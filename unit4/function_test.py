import random
rounds = 0
AI = 0
play = 0
def get_rounds(play,AI):
#    global rounds_e
    rounds = int(input("How many rounds do you want to play? "))
while (rounds != rounds):
    rounds = rounds + 1
def get_p1_move():
#    global play
    play = input("Put Rock, Scissors, Paper: ")
    print (play)
    
def your_pick():
    print("You picked {}:".format(play))
    print("Computer picked {}: ".format(AI))
    
def get_comp_move():
#    global AI
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
def determine_winner():
    ties = 0
    wins = 0
    loses = 0
    if ((play == "Rock" and AI == "Scissors") and
       (play == "Scissors" and AI == "Paper") and
       (play == "Paper" and AI == "Rock")):
        wins = wins + 1
    elif ((AI == "Paper" and play == "Rock") and
         (AI == "Scissors" and play == "Paper") and
         (AI == "Rock" and play == "Scissors")):
         loses = loses + 1
    else:
        print("Tie")
        ties = ties + 1
    if wins == 1:
        print("A winner is you")
    elif loses == 1:
        print("A loser is you")
    elif ties == 1:
        print("a tie is met")

def print_score():
    ties = 0
    wins = 0
    loses = 0
    print("Player Wins: {}".format(wins))
    print("Computer Wins: {}".format(loses))
    print("Ties: {}".format(ties))
def get_round_winner():
    if winner == "play":
        print ("play won")
    elif winner == "AI":
        print ("AI won")
    else:
        print ("tie")
    
def rps():
    winner = 0
    ties = 0
    wins = 0
    loses = 0
    if ((play == "Rock" and AI == "Scissors") and
       (play == "Scissors" and AI == "Paper") and
       (play == "Paper" and AI == "Rock")):
        wins = wins + 1
    elif ((AI == "Paper" and play == "Rock") and
         (AI == "Scissors" and play == "Paper") and
         (AI == "Rock" and play == "Scissors")):
         loses = loses + 1
    else:
        print("Tie")
        ties = ties + 1
    if wins == 1:
        print("A winner is you")
    elif loses == 1:
        print("A loser is you")
    elif ties == 1:
        print("a tie is met")   
     
    rounds = get_rounds()
    play = get_p1_move()
    AI = get_comp_move()
    play = determine_winner()
    winner = get_rounds(play,AI)
    # your_pick()
    # print_score()
    
rps()