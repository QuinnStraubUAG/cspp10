import random
rounds = 0
wins = 0
loses = 0
ties = 0 
AI = 0
play = 0
rounds_e = 0

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

def print_score():
    print("Player Wins: {}".format(wins))
    print("Computer Wins: {}".format(loses))
    print("Ties: {}".format(ties))

def rps():
    # global wins
    # global loses
    # global ties
    
    if get_p1_move() == "Rock" and get_comp_move() == "Scissors":
        print("A winner is you!!! ")
        wins = wins + 1
    elif get_p1_move() == "Scissors" and get_comp_move() == "Paper":
        print("A winner is you!!! ")
        wins = wins + 1
    elif get_p1_move() == "Paper" and get_comp_move() == "Rock":
        print("A winner is you!!! ")
        wins = wins + 1
    elif get_comp_move() == "Paper" and get_p1_move() == "Rock":
        print("A loser is you!!! ")
        loses = loses + 1
    elif get_comp_move() == "Scissors" and get_p1_move() == "Paper":
        print("A loser is you!!! ")
        loses = loses + 1
    elif get_comp_move() == "Rock" and get_p1_move() == "Scissors":
        print("A loser is you!!! ")
        loses = loses + 1
    else:
        print("Tie")
        ties = ties + 1

def your_pick():
    print("You picked {}:".format(play))
    print("Computer picked {}: ".format(AI))

get_rounds()
while (rounds != get_rounds()):
    rounds = rounds + 1
    get_comp_move()
    get_p1_move()
    rps()
    your_pick()
    print_score()