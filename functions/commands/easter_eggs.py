import random

def random_dance():
    dance_moves = ['<(^-^<)','(>^-^)>','<(^-^<)','(>^-^)>','<(^-^<)','(>^-^)>','┻━┻︵ ¯\_(ツ)_/¯︵ ┻━┻']
    randomized_dance = random.shuffle(dance_moves)
    randomized_dance = """
""".join(dance_moves)
    return randomized_dance
