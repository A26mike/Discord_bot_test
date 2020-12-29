import secret 
import discord
import logging

import requests 
import json 


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

#look into api requests and json 
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        quote = get_quote()
        await message.channel.send(quote)


@client.event
async def on_connect():
    print(f' The bot has connected to the server  ')
    
@client.event
async def on_ready():
    print('We have logged in as {0.user} and is ready for use '.format(client))

@client.event
async def on_disconnect():
    print(' The bot has disconnect from server')


        

@client.event
async def on_guild_join(guild):
    for general in guild.text_channels:
        if general and general.permissions_for(guild.me).send_messages:
            await general.send('Hello {}!'.format(guild.name))
            return
    print('I could not send a message in any channel!')


client.run(secret.token)