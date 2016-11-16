import random

rounds = 0
wins = 0
loses = 0
ties = 0 
AI = 0
play = 0
rounds_e = 0
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    #code here
    play = input("Put R,S,P (Must be in caps) ")
    



#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    #code here
    AI = int((random.randint(1,3)))
    if AI == 1:
        AI = "R"
    elif AI == 2:
        AI = "S"
    elif AI == 3:
        AI = "P"
    else:
        print("you broke it")
        
    # print(AI)

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    #code here
    rounds = 0
    rounds_e = int(input("How many rounds do you want to play? "))
    while (rounds != rounds_e):
        rounds = rounds + 1

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's o60 a tie
#    MINE def get_round_winner(p1move, cmove):
    #code here

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
#   MINE def get_full_move():
    #code here

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score():
    #code here
    print("Player Wins: {}".format(wins))
    print("Computer Wins: {}".format(loses))
    print("Ties: {}".format(ties))


#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    #code here
    if play == "R" and AI == "S":
        print("A winner is you!!! ")
        wins = wins + 1
    elif play == "S" and AI == "P":
        print("A winner is you!!! ")
        wins = wins + 1
    elif play == "P" and AI == "R":
        print("A winner is you!!! ")
        wins = wins + 1
    elif AI == "P" and play == "R":
        print("A loser is you!!! ")
        loses = loses + 1
    elif AI == "S" and play == "P":
        print("A loser is you!!! ")
        loses = loses + 1
    elif AI == "R" and play == "S":
        print("A loser is you!!! ")
        loses = loses + 1
    else:
        print("Tie")
    ties = ties + 1

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
#   MINE def test():
    #code here

#   MINE rps()






get_rounds()
while (rounds != rounds_e):
    rounds = rounds + 1
    get_comp_move()
    get_p1_move()
    rps()

















# ignore this I rate 10/10 on IGN


# import random
# rounds = 0
# wins = 0
# loses = 0
# ties = 0 

# rounds_e = int(input("How many rounds do you want to play? "))
# while (rounds != rounds_e):
#     rounds = rounds + 1
#     compu = int((random.randint(1,3)))
#     if compu == 1:
#         compu = "R"
#     elif compu == 2:
#         compu = "S"
#     elif compu == 3:
#         compu = "P"
#     else:
#         print("you broke it")
#     #print(compu)
#     print("Round {}!!!!".format(rounds))
#     play = input("Put R,S,P (Must be in caps) ")
#     print("You picked {}".format(play))
#     print("The computer picked {}".format(compu))
#     if play == "R" and compu == "S":
#         print("A winner is you!!! ")
#         wins = wins + 1
#     elif play == "S" and compu == "P":
#         print("A winner is you!!! ")
#         wins = wins + 1
#     elif play == "P" and compu == "R":
#         print("A winner is you!!! ")
#         wins = wins + 1
#     elif compu == "P" and play == "R":
#         print("A loser is you!!! ")
#         loses = loses + 1
#     elif compu == "S" and play == "P":
#         print("A loser is you!!! ")
#         loses = loses + 1
#     elif compu == "R" and play == "S":
#         print("A loser is you!!! ")
#         loses = loses + 1
#     else:
#         print("Tie")
#         ties = ties + 1
#     print("Player Wins: {}".format(wins))
#     print("Computer Wins: {}".format(loses))
#     print("Ties: {}".format(ties))
# if rounds == rounds_e:
#     print("Thanks for playing")
#Rock beats scissors
#Scissors beats paper
#Paper beats rock




    