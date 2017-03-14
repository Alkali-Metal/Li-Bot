#-----------------------------------------------------------------------------#
#
#
#
#
#
#
#
#
#-----------------------------------------------------------------------------#


"IMPORTS"
import discord
import random



high_chance_dances = [
"<(^-^<)",
"(>^-^)>"
]

low_chance_dances = [
"¯\_(ツ)_/¯",
"┻━┻︵ ノ( ゜-゜ノ)"
]

dance_join = """
"""



not_enough_args = discord.Embed(title="Error", colour=0xFFA60D,
description="Not enough arguments.")
too_many_args = discord.Embed(title="Error", colour=0xFFA60D,
description="Too many arguments.")


def roll(client, message, command, *args):
    if "test" == "poatot":
        print("D3")



def object(client, message, command, *args):
    actions = [client.send_message(message.channel, random.choice(args[1:]))]


def shuffle(client, message, command, *args):
    random_shuffle = random.shuffle(args[1:])
    actions = [client.send_message(message.channel, random_shuffle.join(", "))]
    return actions



def gif(client, message, command, *args):
    actions = [client.send_message(message.channel, random.choice(GIFS))]
    return actions


def alkali(client, message, command, *args):
    alkalis = ["Lithium","Sodium","Potassium","Rubidium","Cesium","Francium"]
    actions = [client.send_message(message.channel, random.choice(alkalis))]
    return actions



"""def dance(client, message, command, *args):
    if len(args) <= 2:
        dance_moves = []
        if len(args) == 2:
            for number in range(0, int(args[1])):
                print(number)
                chances = random.randint(1, 10)
                if chances <= 9:
                    dance_moves.append(random.choice(high_chance_dances))
                elif chances == 10:
                    dance_moves.append(random.choice(low_chance_dances))
            print(dance_moves)
            final_dance = dance_join.join(dance_moves)
            if len(final_dance) <= 2000:
                actions = [client.send_message(message.channel, dance_join.join(dance_moves))]
                return actions
            else:
                actions = [client.send_message(message.channel,
                "Too much dance! (Message too long)")]
                return actions
        else:
            for number in range(0, 5):
                chances = random.randint(1, 10)
                if chances <= 9:
                    dance_moves.append(random.choice(high_chance_dances))
                elif chances == 10:
                    dance_moves.append(random.choice(low_chance_dances))
            final_dance = dance_join.join(dance_moves)
            if len(final_dance) <= 2000:
                actions = [client.send_message(message.channel, dance_join.join(dance_moves))]
                return actions
            else:
                actions = [client.send_message(message.channel,
                "Too much dance! (Message too long)")]
                return actions
    elif len(args) > 2:
        actions = [client.send_message(message.channel, embed=too_many_args)]"""






GIFS = [
"https://giphy.com/gifs/cat-lizard-12Zc0KnExOHsPe",
"https://giphy.com/gifs/reactiongifs-dead-wedding-11eeAFI0e737OM",
"https://giphy.com/gifs/vrFnQhh5VqsUw",
"https://giphy.com/gifs/christmas-bbc-alex-kingston-Zsxh9Cbq7VCy4",
"https://66.media.tumblr.com/a18a316e83f2118a64a7991869d7302a/tumblr_nba2nzm3jj1tyhayao1_500.gif",
"https://giphy.com/gifs/water-heater-zionkBPammlJm",
"https://giphy.com/gifs/jxkfRvvfI0mDm",
"https://giphy.com/gifs/cute-sloth-slothilda-26xoplW0VhLLByrAY",
"https://giphy.com/gifs/horse-applause-clapping-8RxCFgu88jUbe",
"https://giphy.com/gifs/cat-lqtVC9GwItx6M"
]
