import functions.commands.help_messages as messages

def run(server_id):
    if server_id == "145403592113651712":
        return messages.periodic_help_message
    else:
        return messages.normal_help_message
