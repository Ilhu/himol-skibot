import discord
from discord import Member
from discord.ext import commands

import random
import asyncio

ballChoice = ["It is certain.", "As I see it, yes.", "Reply hazy, try again.", "My reply is no",
              "It is decidedly so.", "Most likely.", "Ask again later.", "My sources say no",
              "Without a doubt.", "Yes.", "Better not tell you now.", "Outlook not so good.",
              "Yes - definitely.", "Signs point to yes", "Cannot predict now.", "Very doubtful."]

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(name="8ball")
    async def ball(self, ctx, c: str = None):
        if c is None:
            await ctx.send("What do you want to ask?")
        else:
            await ctx.send(ballChoice[random.randint(0, len(ballChoice)-1)])

def setup(client):
    client.add_cog(Fun(client))
	

