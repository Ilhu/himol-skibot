import discord
from discord import Member
from discord.ext import commands

import random
import asyncio

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def idk(self, ctx):
        msg = await ctx.send("¯\_(ツ)_/¯")
        await asyncio.sleep(0.3)
        await msg.edit(content=r"¯\\–(ツ)–/¯")
        await asyncio.sleep(0.7)
        await msg.edit(content="¯\_(ツ)_/¯")

def setup(client):
    client.add_cog(Fun(client))
	

