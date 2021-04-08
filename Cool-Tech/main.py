import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = !, intents =intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm Ready!")

client.load_extension("cogs.fun")
client.load_extension("cogs.help")
client.load_extension("cogs.mod")
