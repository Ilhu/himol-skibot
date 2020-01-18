import discord
from discord import Client
from discord.ext import commands, tasks
from itertools import cycle
import random
import asyncio
import os

TOKEN = "token"
client = commands.Bot(command_prefix = "-")
status = ["-help - bruh", "-help - WHAT!?!", "-help - pewnews.org", "-help - Area 51", "-help - It's Nerf or nothin'", "-help - Watching Sesame Street", "-help - omnomnom", "-help - Phantom Forces", f"-help - In {len(client.guilds)}servers"]
client.remove_command('help')

@client.event
async def on_ready():
    print("ready on bot.py file")
    status_loop.start()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=10)
async def status_loop():
    await client.change_presence(activity=discord.Game(random.choice(status)))


client.run(TOKEN)
