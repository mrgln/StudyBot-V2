import discord

import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged on as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('ODQyMDQyMDQ1MjI5MDM5NjU5.YJviww.fTPNLBP9vW8U8R1tFaVUZy29k4Q')

token = os.environ.get('BOT_TOKEN')