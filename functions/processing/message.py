import discord
import functions.configs.general_config as config
import functions.processing.permissions as permissions
import functions.processing.server_commands as servers



#class parser:
# Yes I did have the indentation correct for the class, I just undid it before commiting
global lock
lock = "false"



def main(client, message):
    if message.content.startswith(config.command_prefix):
        command, *args = message.content[1:].split()
        if lock == "false":
            print(message.server.name)
            server_name = message.server.name.replace(" ","_")
            print(server_name)
            if message.server.name in servers.server_list:
                if command in servers.server_list[server_name]:
                    permissions = permissions.checking
                    if permissions == "allowed":
                        return servers.server_list[server_name[command]
                            (client, message, *args)]
                    elif permissions == "blocked":
                        return client.send_message(message.channel,
                            "Invalid Permissions")
        elif lock == "true":
            if message.server.id != "219893635439656961":
                return "null"
            elif message.server.id == "219893635439656961":
                return servers.server_list[Bot_Test_Server[command]
                    (client, message, *args)]
    elif message.content.startswith(">"):
        command, *args = message.content[1:].split()
        if command == "lock":
            if lock == "false":
                lock = "true"
            elif lock == "true":
                lock = "false"
            print("The lock has changed to {}".format(lock))
