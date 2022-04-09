import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import os
from discord.ext import commands, tasks
from itertools import cycle
client = commands.Bot(command_prefix=')')
client.remove_command('help')


@client.command()
async def start(ctx):
    global start_channel
    start_channel = ctx.channel.id
    reminder.start()
    print('Reminder Started')


@tasks.loop(seconds=4)
async def reminder():
    embed = discord.Embed  
    channel = client.get_channel(int(962264877420920832))
    await channel.send("L.hentai")


@client.command()
async def stop(ctx):
    reminder.cancel()
    print('Reminder stopped')


@client.command()
async def info(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)
@client.command()
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="Пинг", description=f":ping_pong: Пинг сервера равен **{round(client.latency *1000)}** мс🌎", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="Пинг", description=f":ping_pong: Пинг сервера равен **{round(client.latency *1000)}** мс🌎", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="Пинг", description=f":ping_pong: Пинг сервера равен  **{round(client.latency *1000)}** мс🌎", color=0xff6600)
    else:
        embed=discord.Embed(title="Пинг", description=f":ping_pong: Пинг сервера равен **{round(client.latency *1000)}** мс🌎", color=0x990000)
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='Гнев Бога'):
    await ctx.channel.purge(limit=3)

    await member.kick(reason=reason)
@client.command()
async def version(ctx):
    await ctx.send("Синхронизация с сервером....")
    await asyncio.sleep(5)
    await ctx.send("Kagua v1.1")
 
@client.command()
async def stats(ctx):
    online_members = []
    offline_members = []
    for member in ctx.guild.members:
        if member.status is not discord.Status.offline:
            online_members.append(member.name)
        else:
            offline_members.append(member.name)

    embed = discord.Embed(title=f'"{ctx.guild.name}" Stats', color=0x000)
    embed.add_field(name="Member Count", value=ctx.guild.member_count)
    embed.add_field(name="Online", value=f'{len(online_members)} :green_circle:', inline=True)
    embed.add_field(name="Offline", value =f'{len(offline_members)} :red_circle:', inline = True)
    await ctx.send(embed=embed)   