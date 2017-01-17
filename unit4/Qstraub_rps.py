import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    play = input("Put Rock, Scissors, Paper (or just type R,S,P) (plz in caps): ")
    if play == "Rock":
        print ("You picked Rock")
    elif play == "R":
        print ("You picked Rock")
    elif play == "S":
        print ("You picked Scissors")
    elif play == "Scissors":
        print ("You picked Scissors")
    elif play == "P":
        print ("You picked Paper")
    elif play == "Paper":
        print ("You picked Paper")
    else:
        print("you broke it")
    return play
    

def get_comp_move():
    AI = int((random.randint(1,3)))
    if AI == 1:
        AI = str("Rock")
        print ("The computer picked Rock")
    elif AI == 2:
        print ("The computer picked Scissors")
        AI = str("Scissors")
    elif AI == 3:
        print ("The computer picked Paper")
        AI = str("Paper")
    else:
        print("you broke it")
    return AI

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds = int(input("Number of rounds tell me!!!! "))
    return rounds
    #code here

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner():
    #code here
    p1move = get_p1_move()
    compu = get_comp_move()
    if (p1move == "Rock" and compu == "Scissors") or \
       (p1move == "Paper" and compu == "Rock") or \
       (p1move == "Scissors" and compu == "Paper"):
        return 1
    elif ((compu == "Paper" and p1move == "Rock") or 
         (compu == "Scissors" and p1move == "Paper") or 
         (compu == "Rock" and p1move == "Scissors")):
        return -1
    elif ((compu == "Paper" and p1move == "R") or 
         (compu == "Scissors" and p1move == "P") or 
         (compu == "Rock" and p1move == "S")):
        return -1
    if (p1move == "R" and compu == "Scissors") or \
       (p1move == "P" and compu == "Rock") or \
       (p1move == "S" and compu == "Paper"):
        return 1
    else:
        return 0

def rps():
    rounds = get_rounds()
    P1_score = 0
    P1_score = int(P1_score)
    comp_score = 0
    comp_score = int(comp_score)
    ties = 0
    ties = int(ties)
    for x in range(rounds):
        print ("Round {}!".format(x + 1))
        victory = get_round_winner()
        if victory == 1:
            print("A winner is you")
            P1_score = P1_score + 1
        elif victory == -1:
           print("A loser is you")
           comp_score = comp_score + 1
        else:
            print("A tie has been made")
            ties = ties + 1
            
        print("Player has : {}".format(P1_score))
        print("Computer has : {}".format(comp_score))
        print("The number of tie(s) is {}".format(ties))
        
    if P1_score > comp_score and P1_score > ties:
        print ("The player has won the most")
    elif comp_score > P1_score and comp_score > ties:
        print("The computer has won the most")
    elif ties > P1_score and ties > comp_score:
        print ("There has been more ties then ever")
    else:
        print("Somthing equals somthing else so it is harder to say A kool title")
       

rps()
