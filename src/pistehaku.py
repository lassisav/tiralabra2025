import random

def pistehaku(maara):
    palautus = []
    for i in range(maara):
        palautus.append((random.randint(1, 10000), random.randint(1, 10000)))
    return palautus