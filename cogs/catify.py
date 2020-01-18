from discord import Member, File, TextChannel
from discord.ext import commands
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse

#transforms
CAT_AVATAR_OFFSET = (206, 96)
CAT_AVATAR_SIZE = (280, 280)

COLOR_TRANSPARENT = (255, 0, 0, 0)

cat_raw = Image.open('cat.png').convert('RGBA')

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def catify(self, ctx, cat_user: Member = None):
    	if cat_user is None:
    		cat_user = ctx.author

    	with BytesIO() as avatar_bytes:
    		avatar = cat_user.avatar_url_as(static_format='png')

    		await avatar.save(avatar_bytes)
    		avatar_bytes.seek(0)

    		avatar_image = Image.open(avatar_bytes)
    		avatar_format = avatar_image.format

    		avatar_image = avatar_image.convert('RGBA')

    		avatar_image = avatar_image.resize(CAT_AVATAR_SIZE)

    		cat = cat_raw.copy()

    		cat.paste(avatar_image, CAT_AVATAR_OFFSET)

    		with BytesIO() as final:
    			cat.convert('RGB').save(final, format='PNG')
    			final.seek(0)

    			await ctx.send(file=File(final, filename='catifyed.png'))

def setup(client):
    client.add_cog(Images(client))
