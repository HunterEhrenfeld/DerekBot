import os

import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm.channel.send(
        f'Hi {member.name}, Derek thinks about you when he sleeps!'
    )

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

# @client.event
# async def list_servers():
#     await client.wait_until_ready()
#     while not client.is_closed:
#         print("Current servers:")
#         for server in client.servers:
#             print(server.name)
#         await asyncio.sleep(600)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'derek is hot':
        response = 'He is the cutest'
        await message.channel.send(response)

    if message.content.lower() == 'ping':
        response = 'Pong'
        await message.channel.send(response)

    if message.content.startswith('hello'):
        response = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(response)

client.run(TOKEN)