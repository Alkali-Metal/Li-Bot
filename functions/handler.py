#-------------------------------------------------#
#                                                 #
#  The code that determines what to respond with  #
#                                                 #
#-------------------------------------------------#

import discord
import functions.commands.help as help
import functions.commands.roll as roll
import functions.commands.random as random
import functions.commands.easter_eggs as EEC
import functions.commands.fun as fun
import functions.commands.test as test


def type(command):
    type_of_command = command.info()
    return type_of_command

def user(command, *args, server_id, author_id):
    if command == "test":
        return test.run()
    if command == "help":
        return help.run(server_id=server_id)
    if command == "randomdance":
        return EEC.random_dance()

#def moderator(command, *args):


#def admin(command, *args):
