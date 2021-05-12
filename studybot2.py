import discord

import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged on as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

token = os.environ.get('BOT_TOKEN')

client = MyClient()
client.run(str(token))