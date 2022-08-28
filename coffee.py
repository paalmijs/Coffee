import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="esp")

#Prefix = esp
#Invite link: https://discord.com/oauth2/authorize?client_id=1013465974881660999&scope=bot&permissions=8

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

    if message.content == 'espstory':
        await message.channel.send(f'There really is no story I just like coffee!')

    await bot.process_commands(message)

bot.run('MTAxMzQ2NTk3NDg4MTY2MDk5OQ.GGxKY4.pu2ZT922pvyxdtUBKM4vvhyZ-F8Jkxby2SIbHU')
