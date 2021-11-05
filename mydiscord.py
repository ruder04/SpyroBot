import discord
import spyrocore
from spyrocore import bot_token

client = discord.Client()

@client.event
async def on_ready():
    guild = client.guilds[0]
    print(guild.name, "is the name of the server")
    print(client.user, "has connected to the client")
    
client.run(bot_token)