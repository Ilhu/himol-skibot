import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
import random
import math
import time
import asyncio
import pymongo

myclient = pymongo.MongoClient("database")
database = myclient["Economy"]
e_col = database["users"]

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.usage = ":coinflip <bet>"
        
    @commands.command(pass_context=True)
    async def coinflip(self, ctx, amount: int):
        if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
            await ctx.send("You don't have a bank! Use the `-daily` command to create bank for yourself.")
        else:
            user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
                
            if int(user_bank["bank"]) < amount or amount < 0:
                await ctx.send("You don't have that many cookies in your bank.")
            else:
                r = random.randint(1, 2)
                    
                if r == 1:
                    wonAmount_py = amount * user_bank["multiplier"]
                    wonAmount = int(user_bank["bank"]) + int(float(wonAmount_py))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount_py))
                        
                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(wonAmount), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)

                    await ctx.send(f"You won **{wonAmount_py}** cookie(s)! Awesome!")
                else:
                    currentBank = int(user_bank["bank"]) - amount

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(currentBank)}}

                    e_col.update_one(user_old_ids, user_new_ids)
                    await ctx.send("You lost the coinflip :(")

def setup(client):
    client.add_cog(Games(client))
	
