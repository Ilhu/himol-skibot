import discord
from discord import Member
from discord.ext import commands
import pyfiglet

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ascii(self, ctx, *, arg):
        asciiart = pyfiglet.figlet_format(arg)
        await ctx.send("```" + asciiart + "```")

def setup(client):
    client.add_cog(Fun(client))
