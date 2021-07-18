import discord
import os


from discord.ext import commands
from dotenv import load_dotenv
from util import *

load_dotenv()
bot = commands.Bot(command_prefix='c$')

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command(name='hi')
async def say_hi(ctx):
    await ctx.send('hello there!')


@bot.command(name='info')
async def get_info(ctx , op):
    try:
        data = get_coinInfo(op)
        emb = make_embed_info(data)
        await ctx.channel.send(embed=emb)
    except Exception as e:
        await ctx.channel.send(embed=error_embed())



bot.run(os.getenv('DS_TOKEN'))
