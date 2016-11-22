def rps():
    # global wins
    # global loses
    # global ties
    wins = 0
    loses = 0
    ties = 0
    p1_move = 0
    compu = 0
    # p1_move = get_p1_move()
    # compu = get_comp_move()
    p1_move = ("Rock")
    compu = ("Scissors")
    
    if p1_move == ("Rock") and compu == ("Scissors"):
        #print("A winner is you!!! ")
        wins = wins + 1
    elif p1_move == "Scissors" and compu == "Paper":
        #print("A winner is you!!! ")
        wins = wins + 1
    elif p1_move == "Paper" and compu == "Rock":
        #print("A winner is you!!! ")
        wins = wins + 1
    elif compu == "Paper" and p1_move == "Rock":
        #print("A loser is you!!! ")
        loses = loses + 1
    elif compu == "Scissors" and p1_move == "Paper":
        #print("A loser is you!!! ")
        loses = loses + 1
    elif compu == "Rock" and p1_move == "Scissors":
        #print("A loser is you!!! ")
        loses = loses + 1
    else:
        #print("Tie")
        ties = ties + 1
    if wins == 1:
        return print ("A winner is you!!!")
    elif loses == 1:
        return print ("A loser is you!!!")
    elif ties == 1:
        return print ("A tie has been meet ...")
        

rps()
# def test():
#     return print ("wooooooooo")
    
    
#test()