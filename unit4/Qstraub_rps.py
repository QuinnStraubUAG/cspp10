import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    play = input("Put Rock, Scissors, Paper: ")
    return play
    

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    AI = int((random.randint(1,3)))
    if AI == 1:
        AI = str("Rock")
    elif AI == 2:
        AI = str("Scissors")
    elif AI == 3:
        AI = str("Paper")
    else:
        print("you broke it")
    return AI

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds = input("Number of rounds tell me!!!! ")
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
def get_round_winner(get_p1_move,get_comp_move):
    #code here
    p1move = get_p1_move
    compu = get_comp_move
    if (p1move == "Rock" and compu == "Scissors") or \
       (p1move == "Paper" and compu == "Rock") or \
       (p1move == "Scissors" and compu == "Paper"):
        print ("player")
    elif ((compu == "Paper" and p1move == "Rock") or 
         (compu == "Scissors" and p1move == "Paper") or 
         (compu == "Rock" and p1move == "Scissors")):
        print ("comp")
    else:
        print ("Tie")
    

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
#   Rmind def get_full_move(shortmove):
    #code here

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
#   Rmind def print_score(pscore, cscore, ties):
    #code here

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps(get_rounds, get_comp_move, get_p1_move, get_round_winner):
    rounds = 0
    rounds_g = get_rounds()
    while (rounds != rounds_g):
        rounds = rounds + 1
        get_comp_move()
        get_p1_move()
        get_round_winner(get_p1_move,get_comp_move)
       
        
      
        
    #code here


#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
#   Rmind def test():
    #code here

rps(get_rounds, get_comp_move, get_p1_move, get_round_winner)
#   Rmindget_round_winner(get_p1_move(),get_comp_move())

# Paper
# Scissors
# Rock