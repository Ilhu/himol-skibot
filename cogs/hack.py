import discord
from discord import Member
from discord.ext import commands

import random
import asyncio

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def hack(self, ctx, user: Member = None):
        if user is None:
            user = ctx.message.author.name

        progressText = None
        progress = 0
        
        msg = await ctx.send(f"░░░░░░░░░░ %0 {progressText}")
        
        while progress < 101:
            r = random.randint(1, 3)
            
            if r == 1:
                progress += random.randint(1, 5)

                if progress <= 10:
                    progressText = f"Getting {user}'s IP"
                    await msg.edit(content=f"░░░░░░░░░░ %{progress} {progressText}")
                elif progress >= 10 and progress < 20:
                    await msg.edit(content=f"█░░░░░░░░░ %{progress} {progressText}")
                elif progress >= 20 and progress < 30:
                    await msg.edit(content=f"██░░░░░░░░ %{progress} {progressText}")
                elif progress >= 30 and progress < 40:
                    progressText = f"Cracking {user}'s password"
                    await msg.edit(content=f"███░░░░░░░ %{progress} {progressText}")
                elif progress >= 40 and progress < 50:
                    await msg.edit(content=f"████░░░░░░ %{progress} {progressText}")
                elif progress >= 50 and progress < 60:
                    progressText = f"Establishing a connection on {user}'s network"
                    await msg.edit(content=f"█████░░░░░ %{progress} {progressText}")
                elif progress >= 60 and progress < 70:
                    await msg.edit(content=f"██████░░░░ %{progress} {progressText}")
                elif progress >= 70 and progress < 80:
                    progressText = f"Getting all {user}'s personal info"
                    await msg.edit(content=f"███████░░░ %{progress} {progressText}")
                elif progress >= 80 and progress < 90:
                    await msg.edit(content=f"████████░░ %{progress} {progressText}")
                elif progress >= 90 and progress < 100:
                    progressText = f"Getting {user}'s internet history"
                    await msg.edit(content=f"█████████░ %{progress} {progressText}")
                else:
                    await msg.edit(content=f"██████████ Finished")

                await asyncio.sleep(0.05)

def setup(client):
    client.add_cog(Fun(client))
	

