import functions.handler as handler
import functions.permissions as permissions
import functions.configs.general_config as settings
import discord

client = discord.Client()

def info(a_id, a_name, a_nickname, a_roles, s_id, s_name):
    global author_id, author_name, author_nickname, server_id, server_name, author_roles
    author_id = a_id
    author_name = a_name
    author_nickname = a_nickname
    author_roles = a_roles
    server_id = s_id
    server_name = s_id

def main(command, *args, message):
    permission_level = permissions.permission_level(command, author_roles)
    if permission_level == "user":
        return handler.user(command, args, server_id=server_id)
    elif permission_level == "moderator":
        return handler.moderator(command, args, server_id=server_id)
    elif permission_level == "admin":
        return handler.admin(command, args, server_id=server_id)
    elif permission_level == "no permission":
        return "You don't have access to that command"
