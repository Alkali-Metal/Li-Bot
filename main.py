#-----------------------------------------------------------------------------#
#                                                                             #
#                                                                             #
#                                 Preface:                                    #
#                                                                             #
#     DO NOT CHANGE ANY CODE IN THIS FILE! IF YOU ARE DEVELOPING AND YOU      #
#      MAKE A PULL REQ WITH CODE IN THIS FILE CHANGED IT WILL GET DENIED      #
#                                                                             #
#                                                                             #
#-----------------------------------------------------------------------------#



"IMPORTS"
import asyncio
import discord
import importlib
import functions.processing.processor as parser
import functions.configs.general_config as config



"VARIABLE ASSIGNING"
client = discord.Client()



"CONFIG CHECKING"
if config.command_prefix == "":
    command_prefix = "!"
    print("The command prefix has been set to \"!\"")
if config.respond_to_self != "true":
    respond_to_self = "false"
if config.owner_id == "":
    print("No one will be able to update if you don't add an \"owner_id\" in the general config")
if config.bot_token == "":
    print("The bot cannot login without a bot token! Add one in the general config")



"ON READY"
@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))



"ON MESSAGE"
@client.event
async def on_message(message):
    if message.content.startswith(">"):
        command, *args = message.content[1:].split()
        if message.author.id == config.owner_id:
            if command == "update":
                await client.send_message(message.channel,
                    "Updating the bot :smile:")
                #shutil.rmtree("functions")    COMMENTED TO REDUCE RISK CURRENTLY
                #importlib.reload(functons.parser)
                #importlib.reload(functions.configs.general_config)
            elif command == "reload":
                await client.send_message(message.channel,
                    "Reloading the code! :smiley:")
                importlib.reload(parser)
                importlib.reload(config)
        else:
            await client.send_message(message.channel,
                "You don't have access to that command!")
    elif config.respond_to_self == "true":
        if message.content.startswith(config.command_prefix):
            actions = parser.main(client, message)
            for action in actions:
                await action
                asyncio.sleep(3)
    elif config.respond_to_self == "false":
        if message.author.id != client.user.id:
            if message.content.startswith(config.command_prefix):
                actions = parser.main(client, message)
                for action in actions:
                    await action
                    asyncio.sleep(3)



    "LOGGING IN"
try:
    client.run(config.bot_token)
except:
    print("Error signing into Discord!")

