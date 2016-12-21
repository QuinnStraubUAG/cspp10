def begining_bank():
    print("You have $100 so... Good luck")
    return 100 







def bets ():
    bets_v = int(input("Put in your bets: "))
    #This is return the bet
    return bets_v  







def bets_cal():
    bank_b = begining_bank()
    money = bets()
    while ((money != int(money)) or (money > bank_b) or (money < 1)):
        print("It has to be a whole number, not a negtive, and you need to have enogh money")
        money = bets()
    money = int(money)
    return money
 
def game_thing():
    return 2
        
        
def money_system():
    money_inserted = bets_cal()
    money_inserted = int(money_inserted)
    bank_b = begining_bank()
    bank_b = int(bank_b)
    bank = bank_b
    bank = int(bank)
    win_lose = game_thing()
    
    if win_lose == 1:
        bank = money_inserted * 2 + bank
        print(bank)
    elif win_lose == 2:
        bank = bank - money_inserted
        print (bank)
        
money_system()