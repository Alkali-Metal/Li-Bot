#-----------------------------------------------------------------------------#
#                                                                             #
#                                  Preface:                                   #
#
# 
#
#
#
#
#-----------------------------------------------------------------------------#



"IMPORTS"
import discord
import functions.configs.command_config as command_config


def run(client, message, command, *args):
    actions = []
    for command in command_config.command_helps:
        if command_config.command_helps[command] != "null":
            help_response = command_config.command_helps[command](client, message)
            actions.append(help_response)
    return actions
