import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
import asyncio

import pymongo
myclient = pymongo.MongoClient("database")
database = myclient["Economy"]
e_col = database["users"]

isOnBoost = []

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def shop(self, ctx, choice: int = None):

        if choice == None:
            embed = discord.Embed(
                title = "Shop",
                description = """[ID:1, Price: 70,000] Energy Drink: Increases your multiplier by 5x for 1 minutes\n
                                 [ID:2, Price: 10,000,000] Prostitute: Resets all your cookies, but adds 0.1x to your muliplier permanently"""
                )
            embed.set_footer(text="Example: -shop 1")
            await ctx.send(embed=embed)
        if choice == 1:
            if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
                await ctx.send("You don't have a bank! Use the `:kela` command to create bank for yourself.")
            else:
                user = e_col.find_one({'_id': str(ctx.message.author.id)})
                
                if int(user["bank"]) < 70000:
                    await ctx.send("You don't have that many cookies in your bank.")
                else:
                    if ctx.message.author.id in isOnBoost:
                        await ctx.send("You already have a multiplier effect active.")
                    else:
 
                        currentBank = int(user["bank"]) - 70000

                        user_old_ids = {'_id': str(ctx.message.author.id)}
                        user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(currentBank), 'multiplier': 5.0 + user["multiplier"] - 1.0}}

                        e_col.update_one(user_old_ids, user_new_ids)
                        await ctx.send("Okay, you bought a Energy Drink for 70,000. The effect starts NOW")
                        isOnBoost.append(ctx.message.author.id)
                        await asyncio.sleep(60)
                        isOnBoost.remove(ctx.message.author.id)
                        user_old_ids = {'_id': str(ctx.message.author.id)}
                        user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(currentBank), 'multiplier': 1}}
                        e_col.update_one(user_old_ids, user_new_ids)

        elif choice == 2:
            if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
                await ctx.send("You don't have a bank! Use the `:kela` command to create bank for yourself.")
            else:
                user = e_col.find_one({'_id': str(ctx.message.author.id)})
                
                if int(user["bank"]) < 10000000:
                    await ctx.send("You don't have that many cookies in your bank.")
                else:
                    if ctx.message.author.id in isOnBoost:
                        await ctx.send("You have a multiplier effect active, buy this after it has ended")
                    else:

                        user_old_ids = {'_id': str(ctx.message.author.id)}
                        user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(500), 'multiplier': user["multiplier"] + 0.1}}

                        e_col.update_one(user_old_ids, user_new_ids)
                        await ctx.send("Okay, you bought a Premium Prostitute for 10,000,000. Your stats have been reseted.")
                        isOnBoost.append(ctx.message.author.id)


def setup(client):
    client.add_cog(Economy(client))
