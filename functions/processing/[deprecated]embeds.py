import discord

red = 0xFF0C00
green = 0x00AA00
yellow = 0xFFA60D



###############################################################################

no_permissions = discord.Embed(title="Error!",
description="""You do not have the proper permissions!

Talk to an admin if you think this is wrong.""", colour=red)

###############################################################################

invalid_command = discord.Embed(title="Error", description="Invalid command.",
colour=yellow)

###############################################################################

not_enough_arguments = discord.Embed(title="Error",
description="Not enough arguments.", colour=yellow)

###############################################################################

result = ""
roll_response = discord.Embed(title="Roll Result", description=result,
colour=green)

###############################################################################

one_side_error = discord.Embed(title="Roll Error",
description="I can't roll something with one side!", colour=yellow)

###############################################################################



###############################################################################
