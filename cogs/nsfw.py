import discord
from discord.ext import commands
import random

import asyncio
import rule34

loop = asyncio.get_event_loop()
rule34 = rule34.Rule34(loop)

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="rule34")
    async def rule(self, ctx, *args):
        if ctx.channel.is_nsfw():
            post = await rule34.getImageURLS(tags="{}".format('+'.join(args)))
            r = random.randint(1, len(post))
            print(post[r])
            
            embed = discord.Embed(
                title = "Rule34",
                )
            embed.set_image(url=post[r])
        
            await ctx.send(embed=embed)
        else:
            await ctx.send("Whoa! You need to use this command in a **NSFW** channel!")
 
def setup(client):
    client.add_cog(Help(client))
