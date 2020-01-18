import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
import asyncio

import pymongo
myclient = pymongo.MongoClient("database")
database = myclient["Economy"]
e_col = database["users"]

blackjack = []

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def kela(self, ctx):
        try:
            doc = e_col.find_one({'_id': str(ctx.message.author.id)})
        except:
            print(f"Couldn't find {ctx.message.author}'s id, adding it to database")
        finally:
            if doc:
                money_updated = int(doc["bank"]) + 500
                net_worth_updated = int(doc["net_worth"]) + 500
                old_ids = {"_id": str(ctx.message.author.id)}
                new_ids = {"$set": {"_id": str(ctx.message.author.id), "bank": str(money_updated), "net_worth": str(net_worth_updated)}}
                e_col.update_one(old_ids, new_ids)
                await ctx.send("I added 500 cookies into your bank!")
            else:
                new_ids = {"_id": str(ctx.message.author.id), "bank": str(500), "net_worth": str(500), "multiplier": 1, "acceptTransfer": True}
                e_col.insert_one(new_ids)
                await ctx.send("I added 500 cookies to your brand new bank! Good luck!")



    @commands.command(pass_context=True)
    async def balance(self, ctx, m: Member = None):
        if m == None:
            m = ctx.message.author
            user = "You have"
            user2 = "Your"
        else:
            user = f"{m.name} has"
            user2 = f"{m.name}'s"
        if e_col.find_one({'_id': str(m.id)}) == None:
            await ctx.send("You don't have a bank! Use the `-kela` command to create bank for yourself.")
        else:

            doc = e_col.find_one({'_id': str(m.id)})

            await ctx.send("{} {} cookies in your bank!".format(user, doc["bank"]))
            await ctx.send("{} net worth is {} cookies!".format(user2, doc["net_worth"]))
            await ctx.send("{} muliplier is {}".format(user2, doc["multiplier"]))



    @commands.command(pass_context=True)
    async def transfer(self, ctx, amount: int, id: Member):
        if ctx.message.author.id in blackjack:
            await ctx.send("You need to finish your blackjack game first!")
        else:
            if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
                await ctx.send("You don't have a bank! Use the `-kela` command to create bank for yourself.")
            else:
                if e_col.find_one({'_id': str(id.id)}) == None:
                    await ctx.send("The user who you want to transfer your cookies, doesn't have a bank account.. Tell him/her to create one!")
                else:
                    user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
                    other_bank = e_col.find_one({'_id': str(id.id)})

                    if other_bank["acceptTransfer"] == False:
                        await ctx.send("The user you were trying to send cookies, has disabled transfers.")
                    else:

                        if int(user_bank["bank"]) < amount or amount < 0:
                            await ctx.send("You don't have that many cookies in your bank.")
                        else:
                            userMsg = await self.client.fetch_user(user_id=id.id)
                            await ctx.send("Ok sending the cookies.")
                            await userMsg.send("<@!{}>!, <@!{}> ({}) is transferring you {} cookies. Do you accept? You have 60 seconds.\nREACT WITH :white_check_mark:".format(id.id, ctx.message.author.id, ctx.message.author.id, amount))

                            def check(reaction, user):
                                return user == id and str(reaction.emoji) == '✅'

                            try:
                                reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
                            except asyncio.TimeoutError:
                                await ctx.send('Noone answered...')
                            else:
				
                                user_bank_amount = int(user_bank["bank"]) - amount
                                user_old_ids = {"_id": str(ctx.message.author.id)}
                                user_new_ids = {"$set": {"_id": str(ctx.message.author.id), "bank": str(user_bank_amount)}} 

                                other_bank_amount = int(other_bank["bank"]) + amount
                                other_bank_networth = int(other_bank["net_worth"]) + amount
                                other_old_ids = {"_id": str(id.id)}
                                other_new_ids = {"$set": {"_id": str(id.id), "bank": str(other_bank_amount), "net_worth": str(other_bank_networth)}} 

                                e_col.update_one(user_old_ids, user_new_ids)
                                e_col.update_one(other_old_ids, other_new_ids)

                                await ctx.send("Okay, i sent {} cookies to <@!{}>".format(amount, id.id))


    @commands.command(pass_context=True)
    async def toggletransfer(self, ctx):
        if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
            await ctx.send("You don't have a bank! Use the `-kela` command to create bank for yourself.")
        else:
            user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
            if user_bank["acceptTransfer"] == True:

                user_old_ids = {"_id": str(ctx.message.author.id)}
                user_new_ids = {"$set": {"_id": str(ctx.message.author.id), "acceptTransfer": False}}
                e_col.update_one(user_old_ids, user_new_ids)

                await ctx.send("Okay, you will not receive any transfers.")

            else:

                user_old_ids = {"_id": str(ctx.message.author.id)}
                user_new_ids = {"$set": {"_id": str(ctx.message.author.id), "acceptTransfer": True}}
                e_col.update_one(user_old_ids, user_new_ids)

                await ctx.send("Okay, you will now receive transfers.")


    #ILHU'S OWN CHEAT COMMAND ;DD  
    @commands.command(pass_context=True)
    async def annaperkele(self, ctx, user: Member, amount: int):
        if ctx.message.author.id != 262954793981575169:
            print("ok")
        else:
            try:
                doc = e_col.find_one({'_id': str(user.id)})
            except:
                print(f"Couldn't find {user.id}'s id, adding it to database")
            finally:
                if doc:
                    money_updated = doc["bank"] + amount
                    net_worth_updated = doc["net_worth"] + amount
                    old_ids = {"_id": str(user.id)}
                    new_ids = {"$set": {"_id": str(user.id), "bank": int(money_updated), "net_worth": int(net_worth_updated)}}
                    e_col.update_one(old_ids, new_ids)
                    await ctx.send(f"ok mää lisäsin {user}n accoo {amount} keksii")
                else:
                    new_ids = {"_id": str(user.id), "bank": amount, "net_worth": amount}
                    e_col.insert_one(new_ids)
                    await ctx.send(f"ok mää lisäsin {user}n accoo {amount} keksii")


        
    @kela.error
    async def kela_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
            await ctx.send("You already used your `-kela` command today!")



def setup(client):
    client.add_cog(Economy(client))
