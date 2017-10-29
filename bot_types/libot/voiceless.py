import json

voiceless_path = "data/custom_voiceless_roles.json"

class Voiceless:
    def load():
        with open(voiceless_path, 'r') as file:
            data = json.load(file)
        return data