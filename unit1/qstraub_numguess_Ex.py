import random
last_numb = 1000001
while (last_numb > 1000000):
    last_numb = int(input("Put in a number less than 1,000,000 (Max numb you will guess) "))
    if last_numb > 1000000:
        print ("Your number is too big tell me a smaller one")
randint = int(random.randint(1,last_numb))
x = 0
numb = -1
while (numb != randint):
    x = x + 1
    numb = int(input("Tell me the number you guess (1-100) "))
    if numb > randint :
        print ("Your number is too high ")
        if (x > 60):
            break
    elif numb < randint:
        print("Your number is too low ")
        if (x > 60):
            print ("You guessed too many times")
            break
    elif numb == randint:
        print ("you guessed the number! It took you {} tries".format(x))
    else:
        ("You did your life wrong ")
