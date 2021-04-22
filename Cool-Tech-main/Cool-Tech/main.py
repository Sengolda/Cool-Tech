import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents =intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm Ready!")

extensions = [
    "cogs.fun",
    "cogs.help",
    "cogs.mod"]


for extension in extensions:
    client.load_extension(extension)
    print(f"{extension} has been loaded.")

client.run(input("Put your token:"))