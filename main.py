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
"""



                            Note For Developers:
   Any error code that the code spews out to the terminal should be in the
   following format for easy debugging and finding


                    "startingline-endingline_filename"


    So, that being said, an error from this file might look something like:


                             "119-127_main"


    If you follow this format for print statement errors, you will be happier
                   when people come complaining to you



















"""
#-----------------------------------------------------------------------------#

dragons = """\n
                                                 ,  ,
                                               / \/ \
                                              (/ //_ \_
     .-._                                      \||  .  \
      \  '-._                            _,:__.-"/---\_ \
 ______/___  '.    .--------------------'~-'--.)__( , )\ \
`'--.___  _\  /    |             Here        ,'    \)|\ `\|
     /_.-' _\ \ _:,_          Be Dragons           " ||   (
   .'__ _.' \'-/,`-~`                                |/
       '. ___.> /=,|  Abandon hope all ye who enter  |
        / .-'/_ )  '---------------------------------'
        )'  ( /(/
             \\ "
              '=='
\n
{}
"""



"IMPORTS"
import discord
import asyncio
import importlib
import functions.configs.user_configs.general_config as config
import functions.processing.message as message_parser



"VARIABLE ASSIGNING"
client = discord.Client()
list_thing = []
dict_thing = {}


"CONFIG CHECKING"
if config.bot_token == "":
    token_error = "The bot cannot login without a bot token! Add one in the general config \
                   line 33 in general_config"



"ON READY"
@client.event
async def on_ready():
    print('Logged in as: {user}'.format(user=client.user.name))
    await client.change_presence(game=discord.game(name="with water"))


"ON MESSAGE"
@client.event
async def on_message(message):
    if message.content.startswith(">"):
        if message.channel.is_private == False:
            command, *args = message.content[1:].split()
            if message.author.id in config.owner_ids:
                if command == "update":
                    print("{name} is updating the code from {server}".format(
                    name=message.author.name,
                    server=message.server.name))
                    await client.send_message(message.channel,
                        "Updating the bot :smile:")
                    #shutil.rmtree("functions")    COMMENTED TO REDUCE RISK CURRENTLY
                    #importlib.reload(on_message)
                    #importlib.reload(config)
                elif command == "reload":
                    print("{name} is reloading the code from {server}".format(
                    name=message.author.name,
                    server=message.server.name))
                    await client.send_message(message.channel,
                        "Reloading the code! :smiley:")
                    importlib.reload(message_parser)
                    importlib.reload(config)
                elif command == "lock":
                    if config.locked == True:
                        print("{name} has unlocked the bot from {server}".format(
                        name=message.author.name,
                        server=message.server.name))
                        config.locked = False
                        await client.send_message(message.channel,
                            "The bot is now unlocked")
                    elif config.locked == False:
                        print("{name} has locked the bot from {server}".format(
                        name=message.author.name,
                        server=message.server.name))
                        config.locked = True
                        await client.send_message(message.channel,
                            "The bot is now locked")
            else:
                await client.send_message(message.channel,
                    "That command is restricted to the owners of the bot!")
        else:
            await client.send_message(message.channel,
            "Admin commands must be run from a server")
    else:
        print("Initial Message Initialization")
        if config.respond_to_self == True:
            response = message_parser.main(client, message, config.locked)
            try:
                if type(response) == type(list_thing):
                    for action in response:
                        await action
                else:
                    await response
            except:
                None
        elif config.respond_to_self == False:
            if message.author.id != client.user.id:
                response = message_parser.main(client, message, config.locked)
                try:
                    if type(response) == type(list_thing):
                        for action in response:
                            await action
                    else:
                        await response
                except:
                    None



"LOGGING IN"
try:
    client.run(config.bot_token)
except:
    print(dragons.format(token_error))
