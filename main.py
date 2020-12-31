import secret 
# import discord
# from discord.ext import commands
# import random
# import logging

# import requests 
# import json 

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)


# description = '''An example bot to showcase the discord.ext.commands extension
# module.
# There are a number of utility commands being showcased here.'''

# intents = discord.Intents.all()
# bot = commands.Bot(command_prefix='?', description=description, intents=intents)

# def get_quote():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]['q'] + " -" + json_data[0]['a']
#     return quote
    
# @bot.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$'):
#         quote = get_quote()
#         await message.channel.send(quote)

# @bot.event
# async def on_connect():
#     print(f' The bot has connected to the server  ')
    
# @bot.event
# async def on_ready():
#     print('We have logged in as {0.user} and is ready for use '.format(client))

# @bot.event
# async def on_disconnect():
#     print(' The bot has disconnect from server')

# @bot.event
# async def on_guild_join(guild):
#     for general in guild.text_channels:
#         if general and general.permissions_for(guild.me).send_messages:
#             await general.send('Hello {}!'.format(guild.name))
#             return
#     print('I could not send a message in any channel!')

# @bot.event 
# async def on_member_join(member):
#     pass 

# @bot.event
# async def on_member_remove(member)

# @bot.command()
# async def test(ctx, *args):
#     await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!!', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(secret.token)












