import discord
from discord import Member, Message
from discord.ext import commands
import random
import asyncio
import sys

import pymongo

myclient = pymongo.MongoClient("database")
database = myclient["Economy"]
e_col = database["users"]

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

in_blackjack = []

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(name="blackjack", pass_context=True)
    async def blackjackCommand(self, ctx, amount: int):
        if ctx.message.author.id in in_blackjack:
            await ctx.send("You're already in a game..")
        else:
            if e_col.find_one({'_id': str(ctx.message.author.id)}) == None:
                await ctx.send("You don't have a bank! Use the `-kela` command to create bank for yourself.")
            else:
                user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
                if int(user_bank["bank"]) < amount:
                    await ctx.send("You don't have that many cookies in your bank.")
                else:
                    user_bank = e_col.find_one({'_id': str(ctx.message.author.id)})
                    in_blackjack.append(ctx.message.author.id)

                    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]

                    random.shuffle(deck)

                    userWon = False
                    botWon = False
                    isTimedout = False

                    firstCard = deck[random.randint(0, len(deck))-1]
                    deck.remove(firstCard)
                    secondCard = deck[random.randint(0, len(deck))-1]
                    deck.remove(secondCard)

                    botFirstCard = deck[random.randint(0, len(deck))-1]
                    deck.remove(botFirstCard)
                    botSecondCard = deck[random.randint(0, len(deck))-1]
                    deck.remove(botSecondCard)

                    userDeck = []
                    botDeck = []

                    userDeck.extend((firstCard, secondCard))
                    botDeck.extend((botFirstCard, botSecondCard))

                    def check(reaction, user):
                        return user == ctx.message.author and str(reaction.emoji) == '✅' or str(reaction.emoji) == '✊'
                
                    embed = discord.Embed(
                        title="blackjack",
                        description="WIP(works tho)\n✊=hit\n✅=stand"
                        )
                    botDeck2 = botDeck
                    cardthing = botDeck[0]
                    botDeck[0] = '?'
                    embed.add_field(name="bot", value=f"{botDeck}\nSum: ? + {secondCard}", inline=False)
                    botDeck[0] = cardthing
                    embed.add_field(name=ctx.message.author, value=f"{str(userDeck)}\nSum: {sum(userDeck)}", inline=False)
                    msg = await ctx.send(embed=embed)
                    await msg.add_reaction('✊')
                    await msg.add_reaction('✅')

                    if sum(userDeck) == 21:
                        userWon = True
                    elif sum(userDeck) > 21:
                        botWon = True
                    elif sum(botDeck) == 21:
                        botWon = True
                    elif sum(botDeck) > 21:
                        userWon = True

                    while(userWon == False and botWon == False and isTimedout == False):
                        print(sum(botDeck))
                        print(sum(userDeck))
                        print(userWon)
                        print(botWon)
                        try:
                            reaction, user = await self.client.wait_for('reaction_add', timeout=30, check=check)
                        except asyncio.TimeoutError:
                            isTimedout = True
                        else: 
                            if str(reaction.emoji) == '✊':
                                takeCard = deck[random.randint(0, len(deck))-1]
                                deck.remove(takeCard)
                                userDeck.append(takeCard)
                            elif str(reaction.emoji) == '✅':
                                print("pass")

                            if random.randint(0, 1) == 1:
                                botTakeCard = deck[random.randint(0, len(deck))-1]
                                deck.remove(botTakeCard)
                                botDeck.append(botTakeCard)

                            if sum(userDeck) == 21:
                                userWon = True
                            elif sum(userDeck) > 21:
                                botWon = True
                            elif sum(botDeck) == 21:
                                botWon = True
                            elif sum(botDeck) > 21:
                                userWon = True

                            embed = discord.Embed(
                                title="blackjack",
                                description="WIP(works tho)\n✊=hit\n✅=stand"
                            )
                            embed.add_field(name="bot", value=f"{str(botDeck)}\nSum: {sum(botDeck)}", inline=False)
                            embed.add_field(name=ctx.message.author, value=f"{str(userDeck)}\nSum: {sum(userDeck)}", inline=False)
                            msg = await ctx.send(embed=embed)
                            await msg.add_reaction('✊')
                            await msg.add_reaction('✅')

                    in_blackjack.remove(ctx.message.author.id)

                    if userWon:
                        wonAmount_py = amount * 12 * user_bank["multiplier"]
                        wonAmount = int(user_bank["bank"]) + int(float(wonAmount_py))
                        forNetworth = int(user_bank["net_worth"]) + int(float(wonAmount_py))
                        
                        user_old_ids = {'_id': str(ctx.message.author.id)}
                        user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(wonAmount), 'net_worth': str(forNetworth)}}

                        e_col.update_one(user_old_ids, user_new_ids)

                        await ctx.send(f"You won *{wonAmount_py}* cookies! Awesome!!")
                    elif botWon:
                        currentBank = int(user_bank["bank"]) - amount

                        user_old_ids = {'_id': str(ctx.message.author.id)}
                        user_new_ids = {'$set': {'_id': str(ctx.message.author.id), 'bank': str(currentBank)}}

                        e_col.update_one(user_old_ids, user_new_ids)

                        await ctx.send("You lost your bet.")
                    else:
                        await ctx.send('TIMEOUT, GAME CANCELED')



def setup(client):
    client.add_cog(Economy(client))


