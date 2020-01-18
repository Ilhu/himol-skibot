import discord
from discord.ext import commands

class Allevents(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")
  
def setup(client):
    client.add_cog(Allevents(client))

