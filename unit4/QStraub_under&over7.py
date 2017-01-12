import random

def bets ():
    bets_v = int(input("Put in your bets: "))
    #This is return the bet
    return bets_v  
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    # This randomily rolls two dice and returns there sum

    dice_sum = dice1 + dice2
    
    # print("You rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum
 
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet():
    bank_b = 100
    # Makes sure you do a whole number
    #returns the money you bet
    print ("Your starting with $100 so good luck ... ")
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()
    money = int(money)
    return money

# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range():
    sum = roll2dice()
    sum = int(sum)
    if sum > 7:
        return 2
    elif sum < 7:
        return 0
    else:
        return 1
    # if the sum is over 7, return "over7"
   
    # if the sum is under 7, return "under7"
   
    # if the sum is 7, return "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    key = 0
    while (key == 0):
        player = input("Which will win over7, under7, or 7 (BTW you get more if 7 wins and u pick equal7) so cast your vote today (under7, over7, or equal7) : ")
        if player == ("under7"):
            key = 1
            return 0
        elif player == ("over7"):
            key = 1
            return 2
        elif player == ("equal7"):
            key = 1
            return 1
        else:
            print("You broke it (type better)")
            key = 0
            
            
def game_thing():
    roll = get_range()
    player = choose_range()
    if player == 0 and roll == 0:
        print ("You win its under 7 * insert chessy laugh *")
        return 1
    elif player == 2 and roll == 2:
        print ("You win its over 7 * insert chessy YAY *")
        return 1
    elif player == 1 and roll == 1:
        print ("You win its equals 7 so ... MONEY money money money")
        return 4
# 1 is normal pay out
# 4 is 4 times pay out
    elif player != roll:
        print ("You lost :( ... who am I kidding ha ha get rekt bro wooooooooo")
        return 2
    else: 
        print ("Well its broken ... ")


def money_system():
    #This find out how much money you will have after a win or lose
    #returns your final money count
    fails = 0
    bank = 100
    bank = int(bank)
    money_inserted = get_bet()
    money_inserted = int(money_inserted)
    win_lose = game_thing()
    bank = bank - money_inserted
    
    if win_lose == 1:
        bank = money_inserted * 2 + bank
        print ("Well you won {} dollors so you have {} dollors ".format(money_inserted * 2,bank))
    elif win_lose == 4:
        bank = money_inserted * 4 + bank
        print ("Well you won {} dollors so you have {} dollors ".format(money_inserted * 4,bank))
    elif win_lose == 2:
        print ("Well you lost {} dollors so you have {} dollors left".format(money_inserted,bank))
    else:
        fails = fails + 1
    return (bank)           
    
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
    
    
    
def under_over_7():
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


under_over_7()

    # return their choice
# function for the main game