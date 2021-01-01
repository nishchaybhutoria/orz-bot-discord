import os
import discord
from dotenv import load_dotenv
load_dotenv()
import random
TOKEN = "TOKEN"
client = discord.Client()

hehe = "<:hehe:750745469843538011>"

def hehe():
    s = ""
    for i in range(5):
        for j in range(i+1):
            s += hehe
        s += "\n"
    return s

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'sameple':
        response = "your response"
        await message.channel.send(response)
        
@client.event
async def on_ready():
     print("Connected!")
client.run(TOKEN)
