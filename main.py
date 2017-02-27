import importlib
import discord
import functions.parser as parser
from functions.configs.general_config import owner_id, bot_token, command_prefix


client = discord.Client()


if command_prefix == "":
    command_prefix = "!"


@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))


#def update():
#    if message.content.startswith(">"):
#        if message.author.id == owner_id:
#            await client.send_message(message.channel, "Updating the bot. :smile:")
#            importlib.reload(parser)
#            importlib.reload(functions.configs.general_config)
#        else:
#            await client.send_message(message.channel, "You don't have access to that command")



@client.event
async def on_message(message):
    if message.content.startswith(command_prefix):
        roles = []
        for role in message.author.roles:
            roles.append(role.name)
        command, *args = message.content[1:].split()
        parser.info(a_id=message.author.id, a_name=message.author.name, s_id=message.server.id, a_nickname=message.author.display_name, s_name=message.server.id, a_roles=message.author.roles)
        print(command, args)
        await client.send_message(message.channel, parser.main(command, args, message=message))

client.run(bot_token)
