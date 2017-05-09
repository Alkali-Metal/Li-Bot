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
            return "locked"
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
    if message.author.id in config.owner_ids:
        if command in command_config.direct_only:
            return "allowed"
        elif command in command_config.non_biased:
            return "allowed"
        elif command in command_config.server_only:
            return "server only"
        else:
            return "restricted"
    else:
        if command not in command_config.server_only:
            if command in permissions.user_commands:
                return "allowed"
            else:
                return "disallowed"
        elif command in command_config.server_only:
            return "server only"
        else:
            return "invalid command"
