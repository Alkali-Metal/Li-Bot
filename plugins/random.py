from random import randint

from data.responses import Random as response

from bot_types.libot.config import Config
from bot_types.libot.permissions import Perms

from disco.bot import Plugin
from disco.util.config import Config



class Random(Plugin):
    
    # !random roll [# of dice] <# of sides>
    @Plugin.command("roll", aliases=["number"], group="random")
    def roll_command(self, event):
        
        guild_id = str(event.msg.guild_id)
        arg_count = len(event.args)
        response_rolls = []
        
        config = Config.load("random", guild_id)
        
        if not Perms.has_role(config["allowed_roles"]):
            return event.msg.reply(response.invalid_perms)
        
        config = Config.load("random:roll", guild_id, "command")
        
        if arg_count == 2:
            amount = event.args[0]
            sides = event.args[1]
        else:
            amount = 1
            sides = event.args[0]
        
        if not config["min_sides"] < sides < config["max_sides"]:
            return event.msg.reply(response.side_error.format(config["min_sides"],
                                                            config["max_sides"]))
        elif not config["min_dice"] < amount < config["max_dice"]:
            if arg_count >= 2:
                return event.msg.reply(response.dice_error.format(config["min_dice"],
                                                            config["max_dice"]))
        
        for i in range(1, amount):
            response_rolls.append(random.randint(1, sides))
        
        for i in response_rolls:
            str_rolls.append(str(i))
        
        if amount == 1:
            response_message = response.single_roll.format(sum(response_rolls))
        else:
            response_message = response.multi_roll.format(sum(response_rolls),
                                                           ", ".join(str_rolls))
            if len(response_message) > 2000:
                response_message = response.multi_roll_un.format(sum(response_rolls))
        
        try:
            return event.msg.reply(response_message)
        except:
            return
        
    
    
    #@Plugin.command("formula",aliases=["chemical", "iupac_name"],group="random")
    #def chemical_command(self, event):
    #    
    #    #create configuration function
    #    def config(data):
    #        if str(event.msg.guild_id) in 
    #        configuration = Config.from_file("data/")
    #        if type(data) == type([]):
    #            for i in data:
    #                configuration = configuration.get(i)
    #            return configuration
    #        return configuration.get(data)
    #    
    #    author_roles = event.msg.guild.get_member(event.msg.author).roles
    #    author_roles.append("@everyone")
    #    if not set(author_roles).intersection(config("allowed_roles")):
    #        return
        
        