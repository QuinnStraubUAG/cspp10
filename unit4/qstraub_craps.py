import random

def begining_bank():
    print("You have $100 so... Good luck")
    return 100 
def bets ():
    bets_v = int(input("Put in your bets: "))
    #This is return the bet
    return bets_v  
    
# def bets_Start():
#     B_bank = begining_bank()
#     money_gone = bets()
    
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_sum = dice1 + dice2
    
    print("You rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum

def bets_cal():
    bank_b = begining_bank()
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()
    money = int(money)
    return money
        
        
        

def game_thing():
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
            
        if re == 1 or re == 2
            y_n = input("Do you want to continue [y|n] (No caps plz): ")
            #Run bets code
        else:
            fails = fails + 1
            
        if y_n == "y":
            #Run new func
            print ("I win make win function later")
        elif y_n == "n":
            print("Ok thx for playing")
        else:
            print ("You messed up so now you don't get to go again")
    return re
            

    
            
def money_system():
    money_inserted = bets_cal()
    bank_b = begining_bank()
    bank = bank_b
    win_lose = game_thing()
    if win_lose == 1:
        money_inserted * 2 = bank
    elif win_lose == 2:
        bank = bank - money_inserted
        
        

#  def game_thing_y():
#     roll = dice_roll()
#     fails = 0
#     y_n = 0
#     re = 0
#     if (roll == 2 or roll == 3 or roll == 12):
#         print("You lost")
#         re = 1
#         check = 0 #lose
#     elif (roll == 7 or roll == 11):
#         print("You Win")
#         re = 1
#         check = 1 #win
#     else:
#         check = 2 #point
#         print("You didn't land the things ... POINT ROUND")
#     new_roll = 0
#     point_roll = roll
#     while (check == 2) and (point_roll != new_roll and new_roll != 7):
#         new_roll = dice_roll()
#         print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))
#         if point_roll == new_roll:
#             print("You win your first and Second number matchs")
#             re = 1
#         elif new_roll == 7:
#             print ("You lost you rolled 7")
#             re = 1
#         else:
#             print("It's a draw let's keep going ontil you ether win or lose")
#             input("Press Enter to continue...")
            
#         if re == 1:
#             y_n = input("Do you want to continue [y|n] (No caps plz): ")
#         else:
#             fails = fails + 1
            
#         if y_n == "y":
#             #Run new func
#         elif y_n == "n":
#             print("Ok thx for playing")
#         else:
#             print ("You messed up so now you don't get to go again")
            
                       
        
        
        

        
        
        

def craps():
    bet_test = bets_cal()
    game = game_thing()
   
    
    
    
craps()
    
    
#work in progess
    
    
        
    
     
    
    
 # æææææææ ignorge 
  

  
#   If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends.
# If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends.
# If the player rolls any other number (a 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their “point number“
  
  
  
    
# def funk_test (begining_bank):
#     test = begining_bank()
#     return (test)
    
# funk_test(begining_bank)
