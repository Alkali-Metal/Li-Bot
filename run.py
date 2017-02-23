import discord
import asyncio
import random
import live
#import random_commands.py

"http://multistream.xyz/#Alkali_Metal/QuirkySquid"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------------')

CurrentStatus = "Online"
help = """The help command for Li-Bot:
```!roll [# of dice] [# of sides]
!random <object|number|shuffle>
!test
!alkali
!help
!user
!presence
!blame```"""

@client.event
async def on_message(message):
    global CurrentStatus
    if message.content.startswith('!'):
        command, *args = message.content[1:].split()
        print(command, args)
        if command == "live":
            print(GoingLive())
        if command == "test":
           await client.send_message(message.channel, "Test confirmed:tm:")
        elif command == "user":
            for role in message.server.roles:
                if role.name == "User":
                    await client.add_roles(message.author, role)
        elif command == "stop":
            if message.author.id == "125793782665969664":
                await client.send_message(message.channel, "Shutting down")
                await asyncio.sleep(2)
                await client.close()
            else:
                await client.send_message(message.channel, "You don't have access to that command!")
        elif command == "presence":
            if CurrentStatus == "Do Not Disturb":
                await client.change_presence(game=None, status=discord.Status.invisible)
                CurrentStatus = "Invisible"
                print(CurrentStatus)
            elif CurrentStatus == "Invisible":
                await client.change_presence(game=None, status=discord.Status.dnd)
                CurrentStatus = "Do Not Disturb"
                print(CurrentStatus)
            elif CurrentStatus == "Online":
                await client.change_presence(game=None, status=discord.Status.dnd)
                CurrentStatus = "Do Not Disturb"
                print(CurrentStatus)
            await client.send_message(message.channel, CurrentStatus)
        elif command == "roll":
            if len(args) < 2:
                if len(args) == 0:
                    await client.send_message(message.channel, random.randint(1, 1000000))
                elif len(args) == 1:
                    Sides = int(args[0])
                    if Sides > 1:
                        await client.send_message(message.channel, random.randint(1, Sides))
                    else:
                        await client.send_message(message.channel,"I can't roll a one sided thing!")
            elif len(args) == 2:
                Sides = int(args[1])
                Amount = int(args[0])
                if Amount == 1:
                    if Sides > 1:
                        await client.send_message(message.channel, random.randint(1, Sides))
                    else:
                        await client.send_message(message.channel,"I can't roll a one sided thing!")
                elif Amount > 1:
                    if Sides > 1:
                        Rolls = []
                        for Number in range(Amount):
                            Rolls.append(random.randint(1, Sides))
                        Total = str(sum(Rolls))
                        FRs = ', '.join([str(Roll) for Roll in Rolls])
                        print(Total)
                        CommandThing = "**Total:** " + Total + "     **Rolls:** " + FRs
                        if len(CommandThing) <= 2000:
                            await client.send_message(message.channel, CommandThing)
                        elif len(CommandThing) > 2000:
                            await client.send_message(message.channel, "**Total:** " + Total + "     **Rolls:** Unavailable")
                    else:
                        await client.send_message(message.channel,"I can't roll a one sided thing!")
        elif command == "random":
            if len(args) > 0:
                if args[0] == "object":
                    List = args[1:]
                    if len(List) >= 2:
                        await client.send_message(message.channel, random.choice(List))
                    elif len(List) < 2:
                        await client.send_message(message.channel, "I can't randomly pick between 1 thing!")
                elif args[0] == "number":
                    if len(args) == 1:
                        await client.send_message(message.channel, random.randint(1, 1000000000))
                    elif len(args) == 2:
                        Total = int(args[1])
                        await client.send_message(message.channel, random.randint(1, Total))
                    elif len(args) >= 3:
                        await client.send_message(message.channel, "Too many arguments")
                elif args[0] == "shuffle":
                    if len(args) == 2:
                        await client.send_message(message.channel, "I can't shuffle one thing!")
                    elif len(args) >= 3:
                        Var1 = args[1:]
                        random.shuffle(Var1)
                        await client.send_message(message.channel, ", ".join(Var1))
                    elif len(args) == 1:
                        await client.send_message(message.channel, "Not enough arguments")
                elif len(args) <= 1:
                    await client.send_message(message.channel, "Not enough arguments")
            else:
                await client.send_message(message.channel, "Not enough arguments <object|number|shuffle>")
        elif command == "alkali":
            alkalis = ("Lithium", "Sodium", "Potassium", "Rubidium", "Cesium", "Francium")
            await client.send_message(message.channel, random.choice(alkalis))
        elif command == "blame":
            if message.author.id != "103977657380638720":
                await client.send_message(message.channel, "#Blame" + str(args[0:]).replace("', '", "").replace("['", "").replace("']", ""))
            else:
                await client.send_message(message.channel, "#BlameAbyssin")
        elif command == "help":
            await client.send_message(message.channel, help)







client.run('MjM2NjI2MTIzNDE5NTQ5Njk5.CuL2xg.NDRS6bdM0nHu1HQj0QP1uqVd8lA')
