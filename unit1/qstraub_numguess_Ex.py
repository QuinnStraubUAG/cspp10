import random
last_numb = 1000001
while (last_numb > 1000000):
    last_numb = int(input("Put in a number less than 1,000,000 (Max numb you will guess) "))
    if last_numb > 1000000:
        print ("Your number is too big tell me a smaller one")
randint = int(random.randint(1,last_numb))
x = 0
numb = -1
# numb1 = -1
# numb2 = -1
z = 0
y = 0
while (numb != randint):
    x = x + 1
    numb = int(input("Tell me the number you guess (1-{}) ".format(last_numb)))
    if numb > randint :
        z = z + 1
        # numb1 = numb
        print ("Your number is too high ")
        if z > 3:
            print ("Stop guessing so many high numbers!!! It's annoying!!! TRIGGERED")
        if (x > 60):
            break
    elif numb < randint:
        y = y + 1
        # numb1 = numb
        print("Your number is too low ")
        if y > 3:
            print("Stop guessing so many low numbers!!! It's annoying!!! TRIGGERED")
        if (x > 60):
            print ("You guessed too many times")
            break
    # numb1 = numb2
    # if x % 2 and numb == numb2:
    #     print("You typed the same thing ... you ok you need a break ... need some water bud")
    
    
        # if numb == numb1 and x > 1:
        #     print("You typed the same thing ... you ok you need a break ... need some water bud")
    elif numb == randint:
        print ("you guessed the number! It took you {} tries".format(x))
    else:
        ("You did your life wrong ")
        # beat it in 45 tries


