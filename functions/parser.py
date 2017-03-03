#-------------------------------------------------#
#                                                 #
# The code that determines if you have the proper #
# permissions and to see if it is a valid command #
#                                                 #
#-------------------------------------------------#

import functions.handler as handler
import functions.permissions as permissions
import functions.configs.general_config as settings
import functions.configs.command_config as command_settings

#-----------------------------------------------------------------------------#

def command_type(command, *args):
    print("type parsing")
    if command in command_settings.command_info:
        return command_settings.command_info[command].type()

#-----------------------------------------------------------------------------#

def info(a_id, a_name, a_nickname, a_roles, s_id, s_name):
    global info
    info = []
    info.append(a_id)           #  0
    info.append(a_name)         #  1
    info.append(a_nickname)     #  2
    info.append(a_roles)        #  3
    info.append(s_id)           #  4
    info.append(s_name)         #  5

#-----------------------------------------------------------------------------#

def main(command, *args):
    print("main parser")
    permission_level = permissions.permission_level(command, args, info[3])
    if permission_level == "user":
        return handler.user(command, args, info)
    elif permission_level == "moderator":
        return handler.moderator(command, args, info)
    elif permission_level == "admin":
        return handler.admin(command, args, info)
    elif permission_level == "no permission":
        return "You don't have access to that command"
    elif permission_level == "not a command":
        return "Invalid command."

#-----------------------------------------------------------------------------#
