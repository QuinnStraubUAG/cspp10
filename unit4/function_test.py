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
        
        
        
bets_cal()