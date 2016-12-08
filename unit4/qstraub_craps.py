import random
def bets ():
    bets_v = input("Put in your bets: ")
    #This is return the bet
    return bets_v
  
  
def begining_bank():
    print("You have $100 so... Good luck")

    
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    dice_sum = dice1 + dice2
    
    print("you rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum

def game_thing():
    return 0
    
    
  
  
  
  
  
  
  
  
    
def funk_test (begining_bank):
    test = begining_bank()
    print (test)
    
funk_test(begining_bank)
