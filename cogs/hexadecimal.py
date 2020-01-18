import discord
from discord.ext import commands
import asyncio
import math

class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name="hex")
    async def hexadecimal(self, ctx, number: int):
        await ctx.send(f"The hexadecimal form of {number} is {hex(number)}")

    @hexadecimal.error
    async def hex_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.send("Please specify an integer")
            
def setup(client):
    client.add_cog(Math(client))
