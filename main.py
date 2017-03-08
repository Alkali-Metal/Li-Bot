import importlib
import discord
import functions.parser as parser
import functions.configs.general_config as config



client = discord.Client()



if config.command_prefix == "":
    command_prefix = "!"
    print("The command prefix has been set to \"!\"")
if config.respond_to_self != "true":
    respond_to_self = "false"
    print("The bot will not respond to itself")
if config.owner_id == "":
    print("No one will be able to update if you don't add an \"owner_id\" in the general config")
if config.bot_token == "":
    print("The bot cannot login without a bot token! Add one in the general config")



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
            actions = parser.main(client, message)
            for action in actions:
                await action
    elif config.respond_to_self == "false":
        if message.author.id != client.user.id:
            if message.content.startswith(config.command_prefix):
                actions = await parser.main(client, message)
                for action in actions:
                    await action

        
try:
    client.run(config.bot_token)
except:
    print("Error signing into Discord!")

