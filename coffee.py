import discord

import os

from discord.ext import commands
from discord.utils import get
from discord import TextChannel



client = commands.Bot(command_prefix='*')  # prefix our commands with "*"

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run('MTA0MjgwNDg2MDAxMTE3MTg5MQ.G7z8zV.eDwCGArE4rjWTgRsbdgrEtbl80bAxTR9yCDKEE')