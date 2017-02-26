import discord
#import functions.commands.help as help
#import functions.commands.roll as roll
#import functions.commands.random as random
#import functions.commands.easter_eggs as EEC
#import functions.commands.fun as fun
import functions.commands.test as test

def handler(command, *args, message):
    if command == "test":
        print("User command parsed")
        test.run(message=message)
