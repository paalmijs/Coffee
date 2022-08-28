import discord
from discord.ext import commands

#Prefix = esp
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="^help priekš vairāk informācijas!"))
    print(f'{bot.user} succesfully logged in!')


@bot.event
async def on_message(message):
    # All the bots commands are here!!! :)

    if message.author == bot.user:
        return

    if message.content == 'esptest':
        await message.channel.send(f' response')

    await bot.process_commands(message)

bot.run('')
