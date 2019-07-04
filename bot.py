import discord
from discord.ext import commands
import random
import asyncio
bot = commands.Bot(command_prefix='g!')
bot.remove_command('help')

status = ["OwO", "UwU", "owo", "uwu", "( ͡° ͜ʖ ͡°)"]


@bot.event
async def on_ready():
    while not bot.is_closed():
        seleccionado = random.choice(status)
        print(seleccionado)
        await bot.change_presence(activity=discord.Game(name=seleccionado))
        await asyncio.sleep(60)


@bot.command()
async def spam(ctx, num=3):
    if num > 10:
        num = 10
    for i in range(0, num):
        await ctx.send('@Rubydrag#8207 UwU')


@bot.command()
async def help(ctx):
    mensaje = "```Comandos:\n\tg!spam <numero>: Spamea '@Rubydrag#8207 UwU'. Por defecto lo hara 3 veces pero si especificas un numero lo hara tantas veces como digas\n```"
    await ctx.send(mensaje)


bot.run('NTk2MTA0MDAzMzc3NjkyNjkz.XR0soA.nREk-KstqGWbMXnXnzY96LN-_-s')
