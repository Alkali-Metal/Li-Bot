#-------------------------------------------------#
#                                                 #
# The code that determines if you have the proper #
# permissions and to see if it is a valid command #
#                                                 #
#-------------------------------------------------#

import discord
import functions.errors as errors
import functions.handler as handler
import functions.permissions as permissions
import functions.configs.general_config as settings
import functions.configs.command_config as command_settings
import functions.configs.permissions_config as permission_settings

#-----------------------------------------------------------------------------#

def main(client, message):
    command, *args = message.content[1:].split()
    print(command, args)
    return permission_checks(client, message, command, args)

#-----------------------------------------------------------------------------#

def permission_checks(client, message, command, *args):
    print(command, args)
    permission_final = permissions.permission_level(message, command, args)
    if permission_final == "user":
        return handler.user(client, message, command, args)
    elif permission_final == "moderator":
        return handler.moderator(client, message, command, args)
    elif permission_final == "admin":
        return handler.admin(client, message, command, args)
    elif permission_final == "no permission":
        actions = [client.send_message(message.channel, embed=errors.no_permissions)]
        return actions
    elif permission_final == "not a command":
        actions = [client.send_message(message.channel, embed=errors.invalid_command)]
        return actions

