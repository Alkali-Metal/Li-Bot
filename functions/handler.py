#-------------------------------------------------#
#                                                 #
#  The code that determines what to respond with  #
#                                                 #
#-------------------------------------------------#

import discord
import functions.configs.command_config as commands


def user(command, *args):
    if command in commands.all_commands:
        print("main handler")
        return commands.all_commands[command]()
    elif command in commands.temmie_commands:
        return commands.temmie_commands[command]()


#def moderator(command, *args):


#def admin(command, *args):
