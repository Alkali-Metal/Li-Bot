import discord

red = 0xFF0C00
green = 0x00AA00
yellow = 0xFFA60D



no_permissions = discord.Embed(title="Error!", description="""You do not have the proper permissions!

Talk to an admin if you think this is wrong.""", colour=red)
invalid_command = discord.Embed(title="Error", description="Invalid command", colour=yellow)
