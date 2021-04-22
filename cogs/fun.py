import discord
from discord.ext import commands
import os
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def beers(self, ctx, member : discord.Member):
        await ctx.send("BEER TIME")
        await ctx.send(f"{ctx.author.mention} and {member.mention} hope you enjoy the beer.")


    @commands.command()
    async def add(self, ctx, num1 : int, num2 : int):
        await ctx.send(num1 + num2)

    @commands.command()
    async def remove(self, ctx, num1 : int, num2 : int):
        await ctx.send(num1 - num2)

    @commands.command()
    async def mulitiply(self, ctx, num1 : int, num2 : int):
        await ctx.send(num1 * num2)

    @commands.command()
    async def divide(self, ctx, num1 : int, num2 : int):
        await ctx.send(num1 / num2)


@commands.command(aliases = ['8ball'])
    async def _8ball(ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")



def setup(client):
    client.add_cog(fun(client))
