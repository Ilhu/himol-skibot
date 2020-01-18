import discord
from discord.ext import commands
import asyncio
import random
import compuglobal

simpsons = compuglobal.Frinkiac()

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def simpsonsquote(self, ctx):
        screencap = simpsons.get_random_screencap()
        image = screencap.get_meme_url()
        gif = screencap.get_gif_url()
        r = random.randint(1, 2)

        embed = discord.Embed(
            colour = discord.Colour.gold()
            )

        if r == 1:
            embed.set_image(url=gif)
        else:
            embed.set_image(url=image)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
