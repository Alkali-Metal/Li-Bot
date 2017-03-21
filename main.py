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
import functions.configs.general_config as config
import functions.processing.message as message_parser



"VARIABLE ASSIGNING"
client = discord.Client()


"CONFIG CHECKING"
if config.bot_token == "":
    token_error = "The bot cannot login without a bot token! Add one in the general config"



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
                #importlib.reload(on_message)
                #importlib.reload(config)
            elif command == "reload":
                await client.send_message(message.channel,
                    "Reloading the code! :smiley:")
                importlib.reload(on_message)
                importlib.reload(config)
        else:
            await client.send_message(message.channel,
                "You don't have access to that command!")
    else:
#        try:
        response = message_parser.parser.main(client, message)
        print(response)
        if response == "null":
            print("null response")
        elif type(response) == "list" or type(response) == "set":
            for action in response:
                await action
                await asyncio.sleep(1)
        else:
            await response
            await asyncio.sleep(1)
#        except:
#            print("Message Handling Error")



"LOGGING IN"
try:
    client.run(config.bot_token)
except:
    print(dragons.format(token_error))
