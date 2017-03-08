#-------------------------------------------------#
#                                                 #
#  The code that determines what to respond with  #
#                                                 #
#-------------------------------------------------#

import discord
import functions.configs.command_config as commands


def user(client, message, command, *args):
    if command in commands.all_commands:
        return commands.all_commands[command](client, message, args)
    elif command in commands.temmie_commands:
        return commands.temmie_commands[command](client, message, args)


#def moderator(command, *args):


#def admin(command, *args):
