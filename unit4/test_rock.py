import random
rounds = 0
wins = 0
loses = 0
ties = 0 

rounds_e = int(input("How many rounds do you want to play? "))
while (rounds != rounds_e):
    rounds = rounds + 1
    compu = int((random.randint(1,3)))
    if compu == 1:
        compu = "R"
    elif compu == 2:
        compu = "S"
    elif compu == 3:
        compu = "P"
    else:
        print("you broke it")
    #print(compu)
    print("Round {}!!!!".format(rounds))
    play = input("Put R,S,P (Must be in caps) ")
    print("You picked {}".format(play))
    print("The computer picked {}".format(compu))
    if play == "R" and compu == "S":
        print("A winner is you!!! ")
        wins = wins + 1
    elif play == "S" and compu == "P":
        print("A winner is you!!! ")
        wins = wins + 1
    elif play == "P" and compu == "R":
        print("A winner is you!!! ")
        wins = wins + 1
    elif compu == "P" and play == "R":
        print("A loser is you!!! ")
        loses = loses + 1
    elif compu == "S" and play == "P":
        print("A loser is you!!! ")
        loses = loses + 1
    elif compu == "R" and play == "S":
        print("A loser is you!!! ")
        loses = loses + 1
    else:
        print("Tie")
        ties = ties + 1
    print("Player Wins: {}".format(wins))
    print("Computer Wins: {}".format(loses))
    print("Ties: {}".format(ties))
if rounds == rounds_e:
    print("Thanks for playing")
#Rock beats scissors
#Scissors beats paper
#Paper beats rock




    