import random


def rand():
    a = set()
    while len(a) != 6:
        s = random.randint(1, 16)
        a.add(s)
    return list(a)
