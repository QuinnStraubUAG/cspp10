import random


def begining_bank():
    # This is the amount of money you start with
    # returns money
    return 100 
def bets ():
    bets_v = int(input("Put in your bets: "))
    #This is return the bet
    return bets_v  
    

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    # This randomily rolls two dice and returns there sum

    dice_sum = dice1 + dice2
    
    print("You rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum

def bets_cal():
    bank_b = begining_bank()
    # Makes sure you do a whole number
    #returns the money you bet
    print ("Your starting with $100 so good luck ... ")
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()
    money = int(money)
    return money
        
        
        

def game_thing():
    #The main game ...
    #Returns if you won or lost
    roll = dice_roll()
    fails = 0
    y_n = 0
    re = 0
    if (roll == 2 or roll == 3 or roll == 12):
        print("You lost")
        re = 2
        check = 0 #lose
    elif (roll == 7 or roll == 11):
        print("You Win")
        re = 1
        #runfunction
        check = 1 #win
    else:
        check = 2 #point
        print("You didn't land the things ... POINT ROUND")
    new_roll = 0
    point_roll = roll
    while (check == 2) and (point_roll != new_roll and new_roll != 7):
        new_roll = dice_roll()
        print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))
        if point_roll == new_roll:
            print("You win your first and Second number matchs")
            re = 1
            #runfuction
        elif new_roll == 7:
            print ("You lost you rolled 7")
            re = 2
        else:
            print("It's a draw let's keep going ontil you ether win or lose")
            input("Press Enter to continue...")
    return re
            
def contiune():
    #This ask if you want to play again
    #It returns if you want to play again or not
    fails = 0
    y_n = input("Do you want to continue [y|n] (No caps plz): ")
    while (y_n != "y") and (y_n != "n"):
        y_n = input("Do you want to continue [y|n] (No caps plz): ")
        fails = fails + 1 
    if y_n == "n":
        print ("Thanks for playing better luck next time")
    else: 
        print("Lets keep going")
    return y_n
    

            
def money_system():
    #This find out how much money you will have after a win or lose
    #returns your final money count
    fails = 0
    bank_b = begining_bank()
    bank_b = int(bank_b)
    bank = bank_b
    bank = int(bank)
    money_inserted = bets_cal()
    money_inserted = int(money_inserted)
    win_lose = game_thing()
    bank = bank - money_inserted
    
    if win_lose == 1:
        bank = money_inserted * 2 + bank
        print ("Well you won {} dollors so you have {} dollors ".format(money_inserted * 2,bank))
    elif win_lose == 2:
        print ("Well you lost {} dollors so you have {} dollors left".format(money_inserted,bank))
    else:
        fails = fails + 1
    return (bank)


def craps():
    #This runs the game and runs a new money systerm witch is pretty much the same as the last but your old money will transfer
    fails = 0
    bank = money_system()
    bank = int(bank)
    contin = contiune()
    while contin == "y":
        if bank == 0:
            break
        money_inserted = bets()
        money_inserted = int(money_inserted)
        while ((money_inserted > bank) or (money_inserted < 1)):
            print("It has to be a whole number, not a negtive, and you need to have enogh money")
            money_inserted = bets()
        win_lose = game_thing()
        bank = bank - money_inserted
        if win_lose == 1:
            bank = money_inserted * 2 + bank
            print ("Well you won {} dollors so you have {} dollors ".format(money_inserted * 2,bank))
        elif win_lose == 2:
            print ("Well you lost {} dollors so you have {} dollors left".format(money_inserted,bank))
        else:
            fails = fails + 1
        contin = contiune()
craps()

#work in progess
 # æææææææ ignorge 