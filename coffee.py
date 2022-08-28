import discord

import os

from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL


client = commands.Bot(command_prefix='*')  # prefix our commands with 'esp!'

#Invite link: https://discord.com/oauth2/authorize?client_id=1013465974881660999&scope=bot&permissions=8


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been deleted!")

client.run('')
