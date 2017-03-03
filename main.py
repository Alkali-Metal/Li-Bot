import importlib
import discord
import functions.parser as parser
import functions.configs.general_config as config


client = discord.Client()


if config.command_prefix == "":
    config.command_prefix = "!"

if config.respond_to_self == "":
    config.respond_to_self = "false"

@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))


@client.event
async def on_message(message):
    if message.content.startswith(">"):
        command, *args = message.content[1:].split()
        if command == "update":
            if message.author.id == owner_id:
                await client.send_message(message.channel, "Updating the bot :smile:")
                #shutil.rmtree("functions")    COMMENTED TO REDUCE RISK CURRENTLY
                #importlib.reload(functons.parser)
                #importlib.reload(functions.configs.general_config)
            else:
                await client.send_message(message.channel, "You don't have access to that command!")
    elif config.respond_to_self == "true":
            if message.content.startswith(config.command_prefix):
                command, *args = message.content[1:].split()
                parser.info(a_id=message.author.id, a_name=message.author.name, s_id=message.server.id, a_nickname=message.author.display_name, s_name=message.server.name, a_roles=message.author.roles)
                CType = parser.command_type(message, args)
                if CType == "text":
                    await client.send_message(message.channel, parser.main(command, args))
                elif CType == "file_upload":
                    await client.upload_file(message.channel, parser.main(command, args))
#    elif config.respond_to_self == "false":
#        if message.author.id != client.user.id:

        


client.run(config.bot_token)
