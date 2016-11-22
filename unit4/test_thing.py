import random
rounds = 0
wins = 0
loses = 0
ties = 0 
AI = 0
play = 0
p1_move = ""
compu = ""
rounds_XD = 0

def get_p1_move():
  #  global play
    play = input("Put Rock, Scissors, Paper: ")
    return play
    
def get_comp_move():
    # global AI
    AI = int((random.randint(1,3)))
    if AI == 1:
        AI = "Rock"
    elif AI == 2:
        AI = "Scissors"
    elif AI == 3:
        AI = "Paper"
    else:
        print("you broke it")
    return AI

def get_rounds():
    # global rounds_e
    rounds_e = int(input("How many rounds do you want to play? "))
    return rounds_e

# def print_score():
    # print("Player Wins: {}".format(wins))
    # print("Computer Wins: {}".format(loses))
    # print("Ties: {}".format(ties))

def rps():
    # global wins
    # global loses
    # global ties
    wins = 0
    loses = 0
    ties = 0
    p1_move = get_p1_move()
    compu = get_comp_move()
    
    if p1_move == "Rock" and compu == "Scissors":
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
        return print  ("A winner is you!!!")
    elif loses == 1:
        return print  ("A loser is you!!!")
    elif ties == 1:
        return print  ("A tie has been meet ...")
    else:
        return print ("You broke it ... ")

#def your_pick():
    # print("You picked {}:".format(play))
    # print("Computer picked {}: ".format(AI))

rounds_XD = get_rounds()
while (rounds != rounds_XD):
    rounds = rounds + 1
    get_comp_move()
    get_p1_move()
    rps()
#    your_pick()
#    print_score()
