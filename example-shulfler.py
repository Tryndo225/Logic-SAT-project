import random

L = input("Input to shuffle: ").split(";")

while len(L)>0:
    print(L.pop(random.randrange(len(L))), end=';')