import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help command is ready")

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title="Help Menu")
        em.add_field(name="Moderation", value="`ban`,`kick`,`warn`", inline=True)
        em.add_field(name="Fun", value="`8ball`, `add`,`remove`,`mulitiply`, `divide`,`beers`", inline=True)
        await ctx.send(embed=em)



def setup(client):
    client.add_cog(help(client))