import os
import json

guild_config_dir = "data/guilds/"


class Config:
    
    def has_config(guild_id):
        if str(guild_id) in os.listdir(guild_config_dir):
            return True
        else:
            return False
    
    
    def load(group, guild_id, want="full"):
        guild_id = str(guild_id)
        if want == "full":
            if has_config(guild_id):
                with open("{}/{}.json".format(guild_config_dir, group), 'r') as file:
                    data = json.load(file)
                return data
            else:
                with open("global/{}.json".format(group), 'r') as file:
                    data = json.load(file)
                return data
        elif want == "command":
            group, command = group.split(":")
            if has_config(guild_id):
                with open("{}/{}.json".format(guild_config_dir, group), 'r') as file:
                    data = json.load(file)
                return data[command]
            else:
                with open("global/{}.json".format(group)) as file:
                    data = json.load(file)
                return data[command]