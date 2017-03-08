import functions.configs.permissions_config as config

def permission_level(message, command, *args):
    print(command, args)
    if command in config.all_subcommands:
        if args[0] in config.all_subcommands[command]:
            joining = command, args[0]
            command = "_".join(joining)
        print(command, args)
    roles = []
    for role in message.author.roles:
        roles.append(role.name)
    if command in config.user_commands:
        if config.user_roles.intersection(roles):
            return "user"
        else:
            return "no permission"
    elif command in config.moderator_commands:
        if config.moderator_roles.intersection(roles):
            return "moderator"
        else:
            return "no permission"
    elif command in config.admin_commands:
        if config.admin_roles.intersection(roles):
            return "admin"
        else:
            return "no permission"
    else:
        return "not a command"
