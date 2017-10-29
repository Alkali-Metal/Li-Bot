import json
def load_role_mappings():
    with open('data/custom_voiceless_roles.json', 'r') as file:
        data = json.load(file)
    return data