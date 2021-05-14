import os
import random
import datetime
import discord
from discord.ext import commands

description = "can stay alive without mrgln"

studybot = commands.Bot(
    command_prefix='=',
    description = description,
    help_command = None
    )

token = os.environ.get('BOT_TOKEN')



@studybot.command()
async def ping(ctx):
    a = random.randint(0,4)
    b = 1
    if b == a:
        await ctx.send("gg i've lost 🏓")
    else:
        await ctx.send('pong 🏓')


@studybot.command()
async def rnd(ctx, a: int, b: int):
    """☄️"""
    number = random.randint(a,b)
    await ctx.send(f"Your number is {number}")


@studybot.command()
async def add(ctx, left: int, right: int):
    """☄️"""
    await ctx.send(f"{left} + {right} = {left + right}")
    
@studybot.command()
async def mply(ctx, left: int, right: int):
    """☄️"""
    await ctx.send(f"{left} * {right} = {left * right}")

@studybot.command()
async def div(ctx, left: int, right: int):
    """☄️"""
    await ctx.send(f"{left} / {right} = {left / right}")

@studybot.command()
async def sub(ctx, left: int, right: int):
    """☄️"""
    await ctx.send(f"{left} - {right} = {left - right}")


@studybot.command()
async def sau(ctx):
    await ctx.send('https://wmpics.pics/di-Q6XMW.png')



@studybot.command()
async def help(ctx):
    embed = discord.Embed(title="StudyBot V2", description = 'prefix is "="', timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="🎲 Fun Commands", value="`ping` `rnd`", inline=False)
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