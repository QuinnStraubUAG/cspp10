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
    
    print("You rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
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
        print("I did it")
    elif sum < 7:
        print("I did it")
    else:
        print("I did it")
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
    return 0
   
    # return their choice
get_range() 
# function for the main game