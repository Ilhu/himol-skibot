import discord
from discord.ext import commands
##SET COMMANDS CHANNEL
##:setchannel

import pymongo
myclient = pymongo.MongoClient("database")
database = myclient["set_channels"]
meme_col = database["meme_channels"]

class Setchannel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def memechannel(self, ctx):
        perms: Permission = ctx.message.author.permissions_in(ctx.message.channel)
        try:
            doc = meme_col.find_one({'_id': str(ctx.message.guild.id)})
        except:
            print("can't find")
        finally:
            if perms.administrator:
                if doc:  
                    old_ids = {"_id": str(ctx.message.guild.id), "channel": doc["channel"]}
                    new_ids = {"$set": {"_id": str(ctx.message.guild.id), "channel": str(ctx.message.channel.id)}}
                    meme_col.update_one(old_ids, new_ids)
                    await ctx.send("Okay, I set the channel!")
                else:
                    stuff = {"_id": str(ctx.message.guild.id), "channel": str(ctx.message.channel.id)}
                    meme_col.insert_one(stuff)
                    print("In server: ", ctx.message.guild.id, ", command channel has been set to ", ctx.message.channel.id)
                    await ctx.send("Okay, I set the channel!")
            else:
                await ctx.send("You need to be an administrator to use this command.")

def setup(client):
    client.add_cog(Setchannel(client))


