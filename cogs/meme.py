import discord
from discord.ext import commands

import praw
reddit = praw.Reddit(client_id = "client_id",
                     client_secret = "client_secret",
                     user_agent = "user_agent")

import random
import pymongo
myclient = pymongo.MongoClient("database")
database = myclient["set_channels"]
db_col = database["meme_channels"]

class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name="reddit")
    async def meme(self, ctx, *, arg):
        sreddit = arg
        sub = reddit.subreddit(sreddit).hot(limit=50)
        post = random.randint(0, 50)
        submission = list(sub)[post]
        doc = db_col.find_one({'_id': str(ctx.message.guild.id)})
        if doc:  
            if doc['channel'] == str(ctx.message.channel.id): 
                if submission.over_18:
                    await ctx.send("This is a NSFW command. Please use the NSFW commands instead.")
                else:
                    embed = discord.Embed(
                        title = submission.title,
                        colour = discord.Colour.blue()
                        )
                    
                    embed.set_footer(text=submission.url)
                    embed.add_field(name="Stats", value=":point_up_2: Upvotes: " + str(submission.score) + ", :robot: OP: " + str(submission.author), inline=True)
                    if submission.is_self:
                        if len(submission.selftext) > 1020:
                            embed.add_field(name="Text", value="Here you would see the submission's text, but you don't, because the discord embed field character limit is only 1024 characters, which isn't enough for this post!\nPlease consider upvoting [this](https://support.discordapp.com/hc/en-us/community/posts/360042940911) suggestion, so that it would get more recognition!" , inline=False)
                            await ctx.send(embed=embed)
                        else:
                            embed.add_field(name="Text", value=submission.selftext, inline=False)
                            await ctx.send(embed=embed)

                    elif submission.url[len(submission.url)-3:len(submission.url)] == "jpg" or submission.url[len(submission.url)-3:len(submission.url)] == "png":
                        embed.set_image(url=submission.url)
                        print(submission.url[len(submission.url)-3:len(submission.url)])
                        await ctx.send(embed=embed)
                        
                    else:
                        await ctx.send(embed=embed)
                        await ctx.send(submission.url)
                    
                    #await ctx.send(submission.url + "Heres a r/" + arg + " post")
            else:
                await ctx.send("Wrong channel, use this command where it has been set.")
        else:
            await ctx.send("The channel hasn't been set yet. Use the `:memechannel` command, if you are an admin and haven't set the channel yet.")

    @meme.error
    async def meme_handler(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Please specify the subreddit.")

def setup(client):
    client.add_cog(Meme(client))
