import asyncio
import os
import random
import datetime
import discord
from discord.ext import commands
from discord.ext.commands.core import check

description = "can stay alive without mrgln"

studybot = commands.Bot(
    command_prefix='=',
    description = description,
    help_command = None)

token = os.environ.get('BOT_TOKEN')

def check(author):
    def inner_check(message): 
        if message.author != author:
            return False
        try: 
            int(message.content) 
            return True 
        except ValueError: 
            return False
    return inner_check

@studybot.event
async def on_ready():
    await studybot.change_presence(activity = discord.Game('жизнь (префикс "=")'))

@studybot.command()
async def ping(ctx):
    a = random.randint(0,4)
    b = 1
    if b == a:
        await ctx.send("gg i've lost 🏓")
    else:
        await ctx.send('pong 🏓')


@studybot.command(pass_context = True)
async def guess(ctx):
    number = random.randint(1,6)
    guess = 5
    win = False
    await ctx.send("`У тебя есть пять попыток чтобы угадать число от 1 до 500, выиграешь - получишь роль 'пророк' и будешь находиться отдельно среди списка участников сервера`\nНапиши число:")
    while guess != 0:
        msg = await studybot.wait_for('message',check=check(ctx.author),timeout=30)
        attempt = int(msg.content)
        if attempt>number:
            await ctx.send("`много`")
            await asyncio.sleep(1)
            guess -=1
        elif attempt<number:
            await ctx.send("`мало`")
            await asyncio.sleep(1)
            guess -=1
        elif attempt == number:
            win = True
            await ctx.send("`Ура ты обладаешь силами ванги, поздравляю!`:partying_face:")
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name="пророк")
            await member.add_roles(discord.utils.get(member.guild.roles, name=role))
            break
    if win == False:
        await ctx.send(f'`Число ->{number}`')
        await ctx.send("`Не расстраивайся, ты еще сможешь угадать`:wink:")


@studybot.command()
async def rnd(ctx, a: int, b: int):
    number = random.randint(a,b)
    await ctx.send(f"Your number is {number}")



@studybot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(f"{left} + {right} = {left + right}")
    
@studybot.command()
async def mply(ctx, left: int, right: int):
    await ctx.send(f"{left} * {right} = {left * right}")

@studybot.command()
async def div(ctx, left: int, right: int):
    await ctx.send(f"{left} / {right} = {left / right}")

@studybot.command()
async def sub(ctx, left: int, right: int):
    await ctx.send(f"{left} - {right} = {left - right}")



@studybot.command()
async def sau(ctx):
    await ctx.send('https://wmpics.pics/di-Q6XMW.png')



@studybot.command()
async def help(ctx):
    embed = discord.Embed(title="StudyBot V2", description = 'prefix is "="', timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="🎲 Fun Commands", value="`ping` `rnd` `guess`", inline=False)
    embed.add_field(name="🖩 Math Commands", value="`add` `sub` `mply` `div`",inline=False)
    embed.add_field(name="📋 Schedule Commands", value="sau",inline=False)
    embed.set_image(url='https://avatanplus.ru/files/resources/original/58dd307a43fb515b20055da6.jpg')
    embed.set_footer(text='made by mrgln with <3')
    #embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    await ctx.send(embed=embed)


@studybot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="=)", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    #embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server Region", value="Kazakhstan")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    #embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    await ctx.send(embed=embed)


    
studybot.run(str(token))