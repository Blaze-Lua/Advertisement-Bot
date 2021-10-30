#imports
import discord
from discord.ext import commands
import os

#Setting up OS
token = os.getenv("TOKEN")

#Defining Client and Intents
intents = discord.intents.default()
client = commands.Bot("!" , intents = intents)

#Starting Message
@client.event()
async def on_ready():
    print("Bot Has Logged In")

#Running Bot
client.run(token)