#-----------------------------------------------------------------------------#
#                                                                             #
#                                  Preface:                                   #
#                                                                             #
#                     The response for the "test" command                     #
#                                                                             #
#                                                                             #
#                                                                             #
#                                                                             #
#-----------------------------------------------------------------------------#


import discord
from functions.configs.user_configs.general_config import command_prefix


help_message = discord.Embed(
    colour=0x00AA00,
    title="`{}test` Help".format(command_prefix),
    description="""Checks to make sure the bot is online""")



def run(client, message, command, *args):
    print("MADE IT TO TEST.PY !!!!! HOORAY!")
    actions = [client.send_message(message.author, "Test Confirmed:tm:")]
    return actions




def help(client, message):
    action = client.send_message(message.author, embed=help_message)
    return action
