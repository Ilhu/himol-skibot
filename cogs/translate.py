import discord
from discord import Member
from discord.ext import commands
from googletrans import Translator

trlt = Translator()

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def translate(self, ctx, text: str = None, trltDest: str = None):
        if text == None:
            await ctx.send("What would you like to translate?")
        else:
            if trltDest == None:
                trltDest = "en"

            translatedText = trlt.translate(text, dest=trltDest)
            dtText = trlt.detect(text)
            embed = discord.Embed(
                title = f"Translate {dtText.lang}-{trltDest}",
                description = f"{text}\n--------\n{translatedText.text}"
                )
            await ctx.send(embed=embed)
                
        

def setup(client):
    client.add_cog(Fun(client))
