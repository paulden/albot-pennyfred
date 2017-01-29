import random


def answer_else(content):
    f = open('./phrases.txt')
    lines = f.readlines()
    if "thanks" in content or "thank" in content:
        i = random.randint(0, 2)
        return lines[i]
    elif "batman" in content or "Batman" in content:
        i = random.randint(4, 6)
        return lines[i]
    elif "joke" in content or "jokes" in content:
        i = random.randint(8, 10)
        return lines[i]
    elif "wayne" in content or "Wayne" in content:
        i = random.randint(12, 14)
        return lines[i]
    else:
        return False
