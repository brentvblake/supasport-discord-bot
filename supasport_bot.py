# This example requires the 'message_content' intent.

import discord
import logging
import logging.handlers

#import classes
from classes.f1_api import F1API
from classes.football_api import FootballAPI
from classes.formatting import Formatting

#initialize classes
f1_api = F1API()
football_api = FootballAPI()
formatting = Formatting()

#logging setup
handler = logging.handlers.RotatingFileHandler(
    "supasport_bot.log",
    maxBytes=32*1024*1024, #32MB
    encoding='utf-8',
    backupCount=5 #5 backup logs
)
logging.basicConfig(level=logging.INFO, handlers=[handler])
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')
    print(f'We have logged in as {client.user}')
    
#read token from token.key file
def read_token():
    with open("token.key", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        logging.info(f'Hello command received from {message.author}')
        await message.channel.send('Hello!')
        
    if message.content == ('$day'):
        logging.info(f'Football command received from {message.author}')
        matches = football_api.get_matches_today()
        toSend = formatting.format_game_data_today(matches)
        #send embed message
        await message.channel.send(embed=toSend)
    
    if message.content == ('$week'):
        logging.info(f'Football week command received from {message.author}')
        matches = football_api.get_matches_this_week()
        toSend = formatting.format_game_data_week(matches)
        #send embed message
        await message.channel.send(embed=toSend)
        
    if message.content == ('$last10'):
        logging.info(f'Football last 10 command received from {message.author}')
        matches = football_api.get_last_ten_matches()
        toSend = formatting.format_last_10_games(matches)
        #send embed message
        await message.channel.send(embed=toSend)
        
    if message.content == ('$next10'):
        logging.info(f'Football next 10 command received from {message.author}')
        matches = football_api.get_next_ten_matches()
        toSend = formatting.format_next_ten_games(matches)
        #send embed message
        await message.channel.send(embed=toSend)
    
    if message.content == ('$standings'):
        logging.info(f'Football standings command received from {message.author}')
        standings = football_api.get_standings()
        toSend = formatting.format_league_standings(standings)
        #send embed message
        await message.channel.send(embed=toSend)
        

client.run(read_token(), log_handler=handler)


