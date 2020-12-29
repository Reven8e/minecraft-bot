# © discord.py Minecraft Server Manager- Made by Yuval Simon. For www.bogan.cool

import discord, time, random, string, requests
from discord.ext import tasks, commands
from itertools import cycle
from mcrcon import MCRcon
from secrets import IP, PASSWORD, TOKEN


client = commands.Bot(command_prefix = '.')
status = cycle(['.help for help', 'Best Gen'])
client.remove_command('help')
ROLE = "Pengui"
mcr = MCRcon(IP, PASSWORD)


@client.event
async def on_ready():
    print('Bot is ready.')



@client.command()
@commands.has_role('Mc Admin')
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.green())

    embed.set_author(name='Help- Command List')

    embed.add_field(name='.wt {remove/add} {player}', value="""Add or remove a player from whitelist.""", inline=False)
    embed.add_field(name='.ban {player}', value="""Ban a player.""", inline=False)
    embed.add_field(name='.unban {player}', value="""Unban a player.""", inline=False)
    embed.add_field(name='.kick {player}', value="""Kick a player.""", inline=False)
    embed.add_field(name='.fly {player}', value="""Enable fly mode for a player.""", inline=False)
    
    embed.set_footer(text='© Sky - Made By Reven8e.sh#9290')

    await ctx.send(embed=embed)


@client.command()
@commands.has_role('Mc Admin')
async def wt(ctx, option ,name):
    mcr.connect()
    resp = mcr.command(f"whitelist {option} {name}")
    await ctx.send(f"Done!")
    mcr.disconnect()


@client.command()
@commands.has_role('Mc Admin')
async def ban(ctx, name):
    mcr.connect()
    resp = mcr.command(f"ban {name}")
    await ctx.send(f"Banned {name}")
    mcr.disconnect()


@client.command()
@commands.has_role('Mc Admin')
async def kick(ctx, name):
    mcr.connect()
    resp = mcr.command(f"kick {name}")
    await ctx.send(f"kicked {name}")
    mcr.disconnect()


@client.command()
@commands.has_role('Mc Admin')
async def unban(ctx, name):
    mcr.connect()
    resp = mcr.command(f"unban {name}")
    await ctx.send(f"Unbanned {name}")
    mcr.disconnect()


@client.command()
@commands.has_role('Mc Admin')
async def fly(ctx, name):
    mcr.connect()
    resp = mcr.command(f"fly {name}")
    await ctx.send(f"fly {name}")
    mcr.disconnect()



client.run(TOKEN)