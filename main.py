import importlib
import discord
import functions.parser as parser

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))

"""def update():
    if message.content.startswith("~"):
        if message.author.id == "125793782665969664":
            await client.send_message(message.channel, "Updating the bot. :smile:)
            importlib.reload(.commands.command_reader)
        else:
            await client.send_message(message.channel, "You don't have access to that command")"""

@client.event
async def on_message(message):
    command, *args = message.content[1:].split()
    parser.user(command, args[0:])
#    parser.admin(command, args[0:])

client.run('TOKEN')
