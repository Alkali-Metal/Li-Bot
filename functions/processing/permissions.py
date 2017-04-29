#-----------------------------------------------------------------------------#








#-----------------------------------------------------------------------------#

import functions.configs.user_configs.general_config as config
import functions.configs.user_configs.permission_config as permissions
import functions.configs.developer_configs.command_config as command_config



def public_checking(lock, client, message, command, *args):
    user_roles = []
    for role in message.author.roles:
        user_roles.append(role.name)
    if lock == True:
        if message.server.id in config.lock_override_servers:
            if command not in command_config.direct_only:
                if command in permissions.user_commands:
                    if permissions.user_roles.intersection(user_roles):
                        return "allowed"
                    else:
                        return "disallowed"
                elif command in permissions.moderator_commands:
                    if permissions.moderator_roles.intersection(user_roles):
                        return "allowed"
                    else:
                        return "disallowed"
                elif command in permissions.admin_commands:
                    if permissions.admin_roles.intersection(user_roles):
                        return "allowed"
                    else:
                        return "disallowed"
                else:
                    return "invalid command"
        else:
            print("Locked Server")
    elif lock == False:
        if command not in command_config.direct_only:
            if command in permissions.user_commands:
                if permissions.user_roles.intersection(user_roles):
                    return "allowed"
                else:
                    return "disallowed"
            elif command in permissions.moderator_commands:
                if permissions.moderator_roles.intersection(user_roles):
                    return "allowed"
                else:
                    return "disallowed"
            elif command in permissions.admin_commands:
                if permissions.admin_roles.intersection(user_roles):
                    return "allowed"
                else:
                    return "disallowed"
            else:
                return "invalid command"
        elif command in command_config.direct_only:
            return "null"


def private_checking(client, message, command, *args):
    print("Start of permission checking")
    if message.author.id in config.owner_ids:
        print("Author ID in the config list")
        if command in command_config.direct_only:
            print("Command in direct only - allowed")
            return "allowed"
        elif command in command_config.non_biased:
            print("Command in non-biased - allowed")
            return "allowed"
        elif command in command_config.server_only:
            print("Command in server only - Not allowed")
            return "server only"
    else:
        print("Author ID not in the config as an owner")
        if command not in command_config.server_only:
            print("Command in unbiased or direct only")
            if command in permissions.user_commands:
                print("command in user permission level - allowed")
                return "allowed"
            else:
                print("command not in basic user level - Not allowed")
                return "disallowed"
        elif command in command_config.server_only:
            print("Command is server only")
            return "server only"
        else:
            print("Invalid command response")
            return "invalid command"
