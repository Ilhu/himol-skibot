from discord import Member, File, TextChannel
from discord.ext import commands
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse

#transforms
DOG_AVATAR_OFFSET = (475, 216)
DOG_AVATAR_SIZE = (300, 300)

COLOR_TRANSPARENT = (255, 0, 0, 0)

dog_raw = Image.open('dog.png').convert('RGBA')

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def dogify(self, ctx, dog_user: Member = None):
    	if dog_user is None:
    		dog_user = ctx.author

    	with BytesIO() as avatar_bytes:
    		avatar = dog_user.avatar_url_as(static_format='png')

    		await avatar.save(avatar_bytes)
    		avatar_bytes.seek(0)

    		avatar_image = Image.open(avatar_bytes)
    		avatar_format = avatar_image.format

    		avatar_image = avatar_image.convert('RGBA')

    		avatar_image = avatar_image.resize(DOG_AVATAR_SIZE)

    		dog = dog_raw.copy()

    		dog.paste(avatar_image, DOG_AVATAR_OFFSET)

    		with BytesIO() as final:
    			dog.convert('RGB').save(final, format='PNG')
    			final.seek(0)

    			await ctx.send(file=File(final, filename='dog.png'))

def setup(client):
    client.add_cog(Images(client))
