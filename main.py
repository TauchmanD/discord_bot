import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print(f'We heave logged in as {client}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bruh'):
        if 'iq' in message.content:
            await message.channel.send(f'<@!{message.author.id}> has {random.randint(-45,150)} IQ')        

        if 'penis' in message.content:
            x = random.randint(0,20)
            if x:
                await message.channel.send(f'8{"="*x}D <@!{message.author.id}>')
            else:
                await message.channel.send(f"You don't have a PP <@!{message.author.id}>")
client.run(os.getenv('TOKEN'))