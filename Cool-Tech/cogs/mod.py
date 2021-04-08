import discord
from discord.ext import commands

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod cog is ready")

    @commands.command()
    @commands.has_permssions(ban_members = True)
    async def ban(self, ctx, member : discord.Member,*, reason="reason not given"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.name} has been banned for {reason}")
        await member.send(f"{member.mention} you were banned from {member.guild} for {reason}")



    @commands.command()
    @commands.has_permssions(kick_members = True)
    async def kick(self, ctx, member : discord.Member,*, reason="reason not given"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.name} has been kicked for {reason}")
        await member.send(f"{member.mention} you were kicked from {member.guild} for {reason}")


    @commands.command()
    @commands.has_permssions(kick_members = True)
    async def warn(self, ctx, member : discord.Member,*, reason=None):
        await ctx.send(f"{member.mention} has been wanred for reason.")
        await member.send(f"you were warned in {member.guild} for {reason.}")




def setup(client):
    client.add_cog(mod(client))