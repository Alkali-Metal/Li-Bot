import functions.handler as handler
#import functions.permissions.allowed as permissions
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("~"):
        print("General Parsing Complete")
