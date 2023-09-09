import random


def numero():
    luku1 = int(input("Enter the lower bound: "))
    luku2 = int(input("Enter the upper bound: "))

    return random.randint(luku1,luku2)



print(numero())

