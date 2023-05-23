import datetime

import discord
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
intents.message_content = True

# Erstelle einen Bot-Client
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot ist bereit
@bot.event
async def on_ready():
    print('Bot ist bereit.')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def online(ctx, username:str):
    guild = ctx.guild
    member = get(guild.members, name=username)
    if member is not None:
        await ctx.send(f"Der Nutzer {member.name} wurde gefunden.")
    else:
        await ctx.send("Der angegebene Nutzer wurde nicht gefunden.")

    await ctx.send("Der User " + username + " ist seit ... online")


# Führe den Bot aus
bot.run('MTA3MjEwMjc1MTY0OTE0NDg1Mg.GrVUZX.A5r-4OadxmfELAzFWqYrFy7gve6_v9qYa3XP3M')