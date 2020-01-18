from discord import Member, File, TextChannel
from discord.ext import commands
from PIL import Image, ImageOps, ImageFont, ImageDraw
from io import BytesIO
from urllib.parse import urlparse

COLOR_TRANSPARENT = (255, 0, 0, 0)

kodaCertificate = Image.open('koda_moment.png')

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def kodamoment(self, ctx, koda_user: Member = None):
        if koda_user is None:
            koda_user = ctx.author
        koda = kodaCertificate.copy()
        draw = ImageDraw.Draw(koda)
        font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf", 15)

        draw.text((313, 237), koda_user.author, (255,255,255), font=font)

        with BytesIO() as final:
            koda.save(final, format='PNG')
            final.seek(0)

            await ctx.send(file=File(final, filename='koda_moment.png'))
        

def setup(client):
    client.add_cog(Images(client))
