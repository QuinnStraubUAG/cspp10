def game_thing():
    roll = 7
    if (roll == 2 or roll == 3 or roll == 12):
        print("You lost")
        check = 0 #lose
    elif (roll == 7 or roll == 11):
        print("You Win")
        check = 1 #win
    else:
        check = 2 #point
        
    if check == 1:
        print("Yes")
    else:
        print("no")


game_thing()
# check = 0 = lose
# check = 1 = win
# check = 2 = point