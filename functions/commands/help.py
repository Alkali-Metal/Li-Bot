#-----------------------------------------------------------------------------#
#                                                                             #
#                                  Preface:                                   #
#                                                                             #
#      For each help response from a command file cannot be "return"ed as     #
#                      a list, must be a single object.                       #
#                                                                             #
#                                                                             #
#                                                                             #
#-----------------------------------------------------------------------------#



"IMPORTS"
import discord
from functions.configs.developer_configs import help_config


def run(client, message, command, *args):
    actions = []
    for command in help_config.command_helps:
        if help_config.command_helps[command] != "null":
            help_response = help_config.command_helps[command](client, message)
            actions.append(help_response)
    return actions
