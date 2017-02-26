import functions.handler as handler
import functions.permissions as permissions
import functions.configs.general_config as settings
import discord

client = discord.Client()

def user(command, *args, message):
    if command == "test":
        handler(command, args, message=message)

"""@client.event
async def on_message(message):
    for role in message.author.roles:
        user_roles_local = []
        user_roles_local.append(role)
    set(user_roles_local)

    if user_roles_local.intersection(permissions.user_roles):
        if message.content.startswith("~"):
            print("User Parsing Complete")
    if user_roles.intersection(permissions.moderator_roles):
        if message.content.startswith("~"):
            print("Moderator Parsing Complete")
    if user_roles.intersection(permissions.admin_roles):
        if message.content.startswith("~"):
            print("Admin Parsing Complete")


def handle(message):
    command, *args = message.text.split()
    if settings.admin_roles in message.author.roles:
        return admin(command, *args)
    elif settings.moderator_roles in message.author.roles:
        return moderator(command, *args)
    else:
        return user(command, *args)

handle(message)

"""













