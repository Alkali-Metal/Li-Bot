import importlib
import discord
import functions.parser as parser
from functions.configs.general_config import owner_id, bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))

"""def update():
    if message.content.startswith("~"):
        if message.author.id == owner_id:
            await client.send_message(message.channel, "Updating the bot. :smile:")
            importlib.reload(parser)
        else:
            await client.send_message(message.channel, "You don't have access to that command")"""

@client.event
async def on_message(message):
    command, *args = message.content[1:].split()
    parser.user(command, args, message=message)

client.run(bot_token)
