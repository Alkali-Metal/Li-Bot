#-----------------------------------------------------------------------------#
#                                                                             #
#                                                                             #
#                                 Preface:                                    #
#                                                                             #
#        Within this file is the main handling and parsing for the bot        #
#            along with permission checking and all that fun stuff            #
#                                                                             #
#                                                                             #
#-----------------------------------------------------------------------------#


"IMPORTS"
import discord
import functions.configs.command_config as command_config
import functions.configs.permission_config as permissions_config
from functions.configs.general_config import command_prefix


"VARIABLE DEFINING"

#Colour Defining
colours = {"green":0x00AA00,
"teal":0x0DFF34,
"yellow":0xFFA60D,
"light blue":0x00FFBA,
"dark blue":0x001EFF,
"purple":0x890DFF,
"dark purple":0x6A0DFF,
"magenta":0xB00DFF,
"orange":0xFF3B12,
"red":0xFF0C00}

#Embed Defining
permissions_invalid = discord.Embed(title="Error", colour=colours["red"],
    description="""Invalid Permissions
    
    Talk to an administrator
    if you feel this is wrong""")
invalid_command = discord.Embed(title="Error", colour=colours["yellow"],
    description="""Invalid Command
    
    Run {}help for a command list""".format(command_prefix))





"MESSAGE PARSING"
def main(client, message):
    command, *args = message.content[1:].split()
    if command in command_config.all_commands:
        permission_level = permissions(message)
        if permission_level == "allowed":
            actions = command_config.all_commands[command](client,
                message, command, *args)
            return actions
        elif permission_level == "disallowed":
            actions = [client.send_message(message.channel,
                embed=permissions_invalid)]
            return actions
    elif len(args) != 0:
        joining = command, args[0]
        joined_command = "_".join(joining)
        if joined_command in command_config.all_commands:
            permission_level = permissions(message)
            if permission_level == "allowed":
                return command_config.all_commands[joined_command](client,
                    message, command, *args)
            elif permission_level == "disallowed":
                actions = [client.send_message(message.channel,
                    embed=permissions_invalid)]
                return actions
    else:
        actions = [client.send_message(message.channel, embed=invalid_command)]
        return actions



"PERMISSIONS PARSING"
def permissions(message):
    roles = []
    for role in message.author.roles:
        roles.append(role.name)
    if permissions_config.user_roles.intersection(roles):
        return "allowed"
    elif permissions_config.mod_roles.intersection(roles):
        return "allowed"
    elif permissions_config.admin_roles.intersection(roles):
        return "allowed"
    else:
        return "disallowed"
