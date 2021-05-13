import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='?', intents =intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('logged on as {0}'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

#token = os.environ.get('BOT_TOKEN')

token = "ODQyMDQyMDQ1MjI5MDM5NjU5.YJviww.fTPNLBP9vW8U8R1tFaVUZy29k4Q"

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

#client = MyClient()
bot.run(str(token))