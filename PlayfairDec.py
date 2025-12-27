import random

def exhange2letters(key):
    i = random.randint(0,25)
    j = random.randint(0,25)
    temp = key[i]
    key[j] = temp
    return key
def swap2rows(key):
    i = random.randint(0,5)
    j = random.randint(0,5)
    temp = ''
    for k in range(len(j)):

