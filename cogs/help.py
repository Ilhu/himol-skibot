import discord
from discord.ext import commands
from .nonDiscordCommands.commands import AllCommandUsages

cmds = AllCommandUsages()

allCommands = ["balance", "transfer", "kela", "memechannel", "rule34",
               "reddit", "coinflip", "slots", "dogify", "catify", "computerify",
               "8ball", "hack", "kill", "idk", "rps", "futuramaquote",
               "rickandmortyquote", "simpsonsquote", "sqrt", "hex", "translate"]
		 

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def help(self, ctx, optCommand: str = None):
        if optCommand in allCommands:
            cmdIndex = allCommands.index(optCommand)
            embed = discord.Embed(
                title = "Command Usage",
                description = cmds.commandUsageGetter(optCommand),
                colour = discord.Colour.blue()
                )
            await ctx.send(embed=embed)
        elif optCommand == None:
            embed = discord.Embed(
        		title = "Command list",
        		description = "**Prefix**: -",
        		colour = discord.Colour.blue(),
        		type = "rich"
        		)

            embed.add_field(name=":cookie: Economy", value="`balance, transfer, toggletransfer, kela, slots, coinflip`", inline=False)
            embed.add_field(name=":smirk: NSFW", value="`rule34`", inline=False)
            embed.add_field(name="Image", value="`catify, dogify, computerify`", inline=False)
            embed.add_field(name=":tada: Fun", value="`reddit, rps, kill, hack, idk, 8ball, futuramaquote,\nsimpsonsquote, rickandmortyquote`", inline=False)
            embed.add_field(name="Utility", value="`memechannel, sqrt, hex, translate`", inline=False)
            embed.set_image(url="https://media.giphy.com/media/frATeOuT8QWoazfJmi/giphy.gif")
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text="-help [command name] to check usage")

            await ctx.send(embed=embed)
        else:
            await ctx.send("can't find the command")

def setup(client):
    client.add_cog(Help(client))

