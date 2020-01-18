import discord
from discord import Member
from discord.ext import commands

import random
import asyncio

killPhrases = ["{} got killed by a Minecraft wolf, because he accidentally hit one.",
               "{} challenged Pewdiepie on a Minecraft 1v1. You know what happened next.",
               "{} got killed by an Ender man."]

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.usage = ":kill <member>\nExample: :kill Ilhu/@Ilhu#0500"
        
    @commands.command(pass_context=True)
    async def kill(self, ctx, user: Member = None):
        if user is None:
            user = ctx.message.author.name   
        await ctx.send(killPhrases[random.randint(0, len(killPhrases))].format(user))

def setup(client):
    client.add_cog(Fun(client))
	

