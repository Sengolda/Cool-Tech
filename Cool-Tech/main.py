import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = !, intents =intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm Ready!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    pass 

client.load_extension("cogs.fun")
client.load_extension("cogs.help")
client.load_extension("cogs.mod")