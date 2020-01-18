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
        self.usage = ":slots <bet>"

    @commands.command(pass_context=True)
    async def slots(self, ctx, amount: int):
        if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
            await ctx.send("You don't have a bank! Use the `:kela` command to create bank for yourself.")
        else:
            user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
                
            if int(user_bank["bank"]) < amount or amount < 0:
                await ctx.send("You don't have that many cookies in your bank.")
            else:
                slots = ['chocolate_bar', 'cookie', 'tangerine', 'apple', 'cherries', 'seven']

                slot4 = slots[random.randint(0, 5)]
                slot5 = slots[random.randint(0, 5)]
                slot6 = slots[random.randint(0, 5)]
        
                slot1 = slots[random.randint(0, 5)]
                slot2 = slots[random.randint(0, 5)]
                slot3 = slots[random.randint(0, 5)]
        
                slot7 = slots[random.randint(0, 5)]
                slot8 = slots[random.randint(0, 5)]
                slot9 = slots[random.randint(0, 5)]

                slotOutput1 = '|:{}:|:{}:|:{}:|'.format(slot1, slot2, slot3)
                slotOutput2 = '|:{}:|:{}:|:{}:|'.format(slot4, slot5, slot6)
                slotOutput3 = '|:{}:|:{}:|:{}:|'.format(slot7, slot8, slot9)

                if slot1 == 'seven' and slot5 == 'seven' and slot9 == 'seven':
                    wonAmount = (amount * 100) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)


                elif slot3 == 'seven' and slot5 == 'seven' and slot7 == 'seven':
                    wonAmount = (amount * 100) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)

            
                elif slot1 == 'seven' and slot2 == 'seven' and slot3 == 'seven':
                    wonAmount = (amount * 100) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"JACKPOT, you won {wonAmount} cookies! Good job!!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)

                elif slot4 == 'seven' and slot5 == 'seven' and slot6 == 'seven':
                    wonAmount = (amount * 100) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"JACKPOT, you won {wonAmount} cookies! Good job!!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)

                elif slot7 == 'seven' and slot8 == 'seven' and slot9 == 'seven':
                    wonAmount = (amount * 100) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"JACKPOT, you won {wonAmount} cookies! Good job!!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)

                elif slot1 == slot5 and slot5 == slot9 and slot9 != 'seven':
                    wonAmount = (amount * 7) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)


                elif slot3 == slot5 and slot5 == slot7 and slot7 != 'seven':
                    wonAmount = (amount * 7) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)



                elif slot1 == slot2 and slot2 == slot3 and slot3 != 'seven':
                    wonAmount = (amount * 7) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)


                elif slot4 == slot5 and slot5 == slot6 and slot6 != 'seven':
                    wonAmount = (amount * 7) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)


                elif slot7 == slot8 and slot8 == slot9 and slot9 != 'seven':
                    wonAmount = (amount * 7) * user_bank["multiplier"]

                    forBank = int(user_bank["bank"]) + int(float(wonAmount))
                    forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount))
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + f"Nice, you won {wonAmount} cookies!")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(forBank), 'net_worth': str(forNetworth)}}

                    e_col.update_one(user_old_ids, user_new_ids)


                    
                else:
                    lostAmount = int(user_bank["bank"]) - amount
                    
                    msg = await ctx.send(f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3)
                    await asyncio.sleep(1)
                    await msg.edit(content=f":slot_machine: Slots :slot_machine:\nBet = {amount}\n\n" + slotOutput1 + "\n" + slotOutput2 + "\n" + slotOutput3 + "\n\n" + "You won nothing.. :(")

                    user_old_ids = {'_id': str(ctx.message.author.id)}
                    user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(lostAmount)}}

                    e_col.update_one(user_old_ids, user_new_ids)

def setup(client):
    client.add_cog(Games(client))
	
