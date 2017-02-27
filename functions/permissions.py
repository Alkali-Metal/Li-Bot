import functions.configs.permissions_config as config

def permission_level(command, author_roles):
    roles = []
    for role in author_roles:
        roles.append(role.name)
    if command in config.user_commands:
        if config.user_roles.intersection(roles):
            return "user"
        else:
            return "no permission"
    if command in config.moderator_commands:
        if config.moderator_roles.intersection(roles):
            return "moderator"
        else:
            return "no permission"
    if command in config.admin_commands:
        if config.admin_roles.intersection(roles):
            return "admin"
        else:
            return "no permission"
