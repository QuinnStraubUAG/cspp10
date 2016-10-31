import random
randint = int(random.randint(1,100))
x = 0
numb = -1
while (numb != randint):
    x = x + 1
    numb = int(input("Tell me the number you guess (1-100) "))
    if numb > randint :
        print ("Your number is too high ")
    elif numb < randint:
        print("Your number is too low ")
    elif numb == randint:
        print ("you guessed the number! It took you {} tries".format(x))
    else:
        ("You did your life wrong ")
    