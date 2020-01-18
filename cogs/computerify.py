from discord import Member, File, TextChannel
from discord.ext import commands
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse

#transforms
COMPUTER_AVATAR_OFFSET = (341, 131)
COMPUTER_AVATAR_SIZE = (299, 218)

COLOR_TRANSPARENT = (255, 0, 0, 0)

computer_raw = Image.open('computer.png').convert('RGBA')

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def computerify(self, ctx, computer_user: Member = None):
    	if computer_user is None:
    		computer_user = ctx.author

    	with BytesIO() as avatar_bytes:
    		avatar = computer_user.avatar_url_as(static_format='png')

    		await avatar.save(avatar_bytes)
    		avatar_bytes.seek(0)

    		avatar_image = Image.open(avatar_bytes)
    		avatar_format = avatar_image.format

    		avatar_image = avatar_image.convert('RGBA')

    		avatar_image = avatar_image.resize(COMPUTER_AVATAR_SIZE)

    		computer = computer_raw.copy()

    		computer.paste(avatar_image, COMPUTER_AVATAR_OFFSET)

    		with BytesIO() as final:
    			computer.convert('RGB').save(final, format='PNG')
    			final.seek(0)

    			await ctx.send(file=File(final, filename='computer.png'))

def setup(client):
    client.add_cog(Images(client))
