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


@client.event
async def on_message(message):
    if message.content.startswith(">"):
        if message.author.id == owner_id:
            await client.send_message(message.channel, "Updating the bot :smile:")
            #shutil.rmtree("functions")    COMMENTED TO REDUCE RISK CURRENTLY
            #importlib.reload(functons.parser)
            #importlib.reload(functions.configs.general_config)
        else:
            await client.send_message(message.channel, "You don't have access to that command!")
    elif message.content.startswith(command_prefix):
        command, *args = message.content[1:].split()
        print(command, args)
        parser.info(a_id=message.author.id, a_name=message.author.name, s_id=message.server.id, a_nickname=message.author.display_name, s_name=message.server.id, a_roles=message.author.roles)
        #command_type = parser.command_type(command)
        #if command_type == "text":
        await client.send_message(message.channel, parser.main(command, args, message=message))
        #elif command_type == "role_assignment":
        #    await client.add_roles(message.channel, parser.main(command, args, message=message))
        #elif command_type == "file_upload":
        #    await client.upload_file(message.channel. parser.main(command, args, message=message))
#        elif command_type == "":


client.run(bot_token)
