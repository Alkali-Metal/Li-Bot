#-----------------------------------------------------------------------------#








#-----------------------------------------------------------------------------#


import functions.processing.permissions as permission
import functions.configs.user_configs.general_config as config
import functions.processing.config_checks as config_checking
from functions.configs.developer_configs import command_config



def main(client, message, lock, *args):
    if message.channel.is_private == False:
        print("Message in Server")
        if message.server.id in config.server_command_prefix:
            if message.content.startswith(config.server_command_prefix[
                message.server.id]):
                return handling(lock, client, message, *args)
        elif message.content.startswith(config.command_prefix):
            return handling(lock, client, message, *args)
    else:
        print("Direct Message")
        if message.content.startswith(config.command_prefix):
            handling(lock, client, message, *args)

def handling(lock, client, message, *args):
    print("Handler")
    command, *args = message.content[1:].split()
#    print(command, args)
    if message.channel.is_private == False:
        print("Public Channel - Public Checking")
        permission_level = permission.public_checking(lock, client, message,
            command, *args)
    elif message.channel.is_private == True:
        print("Direct Channel - Private Checking")
        permission_level = permission.private_checking(client, message,
            command, *args)
    else:
        print("Channel Type Not Supported Yet")
#   Executing the command if permissions allow
    if permission_level == "allowed":
        print("Has returned \"allowed\"")
        if command in command_config.non_biased:
            return command_config.non_biased[command](client, message, command,
                *args)
        elif command in command_config.server_only:
            return command_config.server_only[command](client, message, command,
                *args)
        elif command in command_config.direct_only:
            return command_config.direct_only[command](client, message, command,
                *args)
    elif permission_level == "disallowed":
        print("Has returned \"disallowed\"")
        return client.send_message(message.channel, "Invalid permissions")
    elif permission_level == "invalid command":
        print("Has returned \"Invalid command\"")
        return client.send_message(message.channel, "Invalid command")
    elif permission_level == "server only":
        print("Has returned \"server only\"")
        return client.send_message(message.channel, "That command is server only")
    elif permission_level == "restricted":
        print("Has returned \"resticted\"")
        return client.send_message(message.channel, "That command is restricted")
    elif permission_level == "null":
        print("Has returned \"null\"")
        return None
    else:
        print("PANIC AND RUN!")
        print("Invalid permission response")