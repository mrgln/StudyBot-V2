# import discord

# import os

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

    

# token = os.environ.get('BOT_TOKEN')

# client.run(str(token))
import os
import discord
from discord.ext import commands

studybot = commands.Bot(command_prefix='=')
token = os.environ.get('BOT_TOKEN')

@studybot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@studybot.command()
async def img(ctx):
    await ctx.send('https://wmpics.pics/di-PPUG.png')

studybot.run(str(token))