import discord
from discord.ext import commands
import asyncio
import math

class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name="sqrt")
    async def squareroot(self, ctx, number: int):
        await ctx.send(f"The square root of {number} is {math.sqrt(number)}")

    @squareroot.error
    async def squareroot_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.send("Please specify an integer")

def setup(client):
    client.add_cog(Math(client))
