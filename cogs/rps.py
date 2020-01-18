import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown

import random
import math
import time
import asyncio

choice = ["rock", "paper", "scissors"]
choiceEmoji = [":rock:", ":paper", ":scissors:"]

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.usage = ":rps <rock/paper/scissors>"
        
    @commands.command(pass_context=True)
    async def rps(self, ctx, player):
        computerChoice = random.randint(0, 2)
        computer = choice[computerChoice]

        if player == "rock":
            playerEmoji = 0
        elif player == "paper":
            playerEmoji = 1
        else:
            playerEmoji = 2

        embed = discord.Embed(
            colour = discord.Colour.blue()
            )
        
        if player == computer:
            embed.add_field(name="Tie", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
            await ctx.send(embed=embed)
            
        elif player == "rock":
            if computer == "paper":
                embed.add_field(name="Loss", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)
            else:
                embed.add_field(name="Win", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)
                
        elif player == "paper":
            if computer == "scissors":
                embed.add_field(name="Loss", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)
            else:
                embed.add_field(name="Win", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)

        elif player == "scissors":
            if computer == "rock":
                embed.add_field(name="Loss", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)
            else:
                embed.add_field(name="Win", value="{}: {} {} \nKyle: {} {}".format(ctx.message.author.name, player, choiceEmoji[playerEmoji], computer, choiceEmoji[computerChoice]), inline=False)
                await ctx.send(embed=embed)

        else:
            await ctx.send("You need to choose rock, paper, or scissors dude")
            
def setup(client):
    client.add_cog(Games(client))
	
