# This example requires the 'message_content' intent.

import discord
import logging
import logging.handlers

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

client.run(read_token(), log_handler=handler)


