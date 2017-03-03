import random



#-----------------------------------------------------------------------------#

def type():
    return "text"

#-----------------------------------------------------------------------------#

def dance(*args):
#    total_moves = 0
#    while total_moves <= args[1]
     print("HI!")
#-----------------------------------------------------------------------------#

def roll(*args):
    if len(args) < 2:
        if len(args) == 0:
            return random.randint(1, 1000000)
        elif len(args) == 1:
            Sides = int(args[0])
            if Sides > 1:
                return random.randint(1, Sides)
            else:
                return "I can't roll a one sided thing!"
    elif len(args) == 2:
        Sides = int(args[2])
        Amount = int(args[3])
        if Amount == 1:
            if Sides > 1:
                return random.randint(1, Sides)
            else:
                return "I can't roll a one sided thing!"
        elif Amount > 1:
            if Sides > 1:
                Rolls = []
                for Number in range(Amount):
                    Rolls.append(random.randint(1, Sides))
                Total = str(sum(Rolls))
                FRs = ', '.join([str(Roll) for Roll in Rolls])
                roll_response = "**Total:** " + Total + "     **Rolls:** " + FRs
                if len(CommandThing) <= 2000:
                    return roll_response
                elif len(roll_response) > 2000:
                    roll_response2 = "**Total:** " + Total + "  **Rolls:** Unavailable"
                    return roll_response2
            else:
                return "I can't roll a one sided thing!"
    else:
        return "Not enough arguments"

#-----------------------------------------------------------------------------#

def number(*args):
    if len(args) == 2:
        return random.randint(0, args[1])
    elif len(args) < 2:
        return "Not Enough Arguments"
    elif len(args) > 2:
        return "Too Many Arguments" 

#-----------------------------------------------------------------------------#

def object(*args):
    return random.object(args[1:])

#-----------------------------------------------------------------------------#

def shuffle(*args):
    random_shuffle = random.shuffle(args[1:])
    return random_shuffle.join(", ")

#-----------------------------------------------------------------------------#

def alkali():
    alkalis = {"Lithium","Sodium","Potassium","Rubidium","Cesium","Francium"}
    return random.choice(alkalis)

#-----------------------------------------------------------------------------#
