def get_p1_move():
    while True:
        player = input("Rock, Paper or Scissors? (Input as written): ")
        if player == "Rock":
            return "r"
        elif player == "Paper":
            return "p"
        elif player == "Scissors":
            return "s"
        else:
            print(" I couldn't understand, please try that thing again ")

def get_comp_move():
    comp = random.randint(1,3)
    if comp == 1:
        return "r"
    elif comp == 2:
        return "p"
    elif comp == 3:
        return "s"

def get_rounds():
    rounds = int(input("How many rounds would you like to play? (1-9): "))
    return rounds

def get_round_winner(player, comp):
    if player == comp:
        return "tie"
    elif player == "r" and comp == "s":
        return "player"
    elif player == "r" and comp == "p":
        return "comp"
    elif player == "p" and comp == "r":
        return "player"
    elif player == "p" and comp == "s":
        return "comp"
    elif player == "s" and comp == "p":
        return "player"
    elif player == "s" and comp == "r":
        return "comp"

def get_full_move(shortmove):
    if shortmove == "r":
        return "Rock"
    elif shortmove == "p":
        return "Paper"
    elif shortmove == "s":
        return "Scissors"

def print_score(pscore, cscore, ties):
    return "The score is Player 1: {}, Player 2: {}, and {} ties.".format(pscore,cscore,ties)

def rps():
    print("Welcome to the game Rock, Paper, Scissors!")
    print("--------------------------")
    rounds = get_rounds()
    pscore = 0
    cscore = 0
    ties = 0
    for x in range(rounds):..............
        print ("Round {}!".format(x + 1))
        player = get_p1_move()
        comp = get_comp_move()
    
        print("Player chose: {}".format(get_full_move(player)))
        print("Computer chose: {}".format(get_full_move(comp)))
    
        winner = get_round_winner(player,comp)
        if winner == "player":
            print("The Player won!!!")
            pscore = pscore + 1
        elif winner == "comp":
            print("The Computer won!!!!")
            cscore = cscore + 1
        else:
            print("It's a tie")
            ties = ties + 1
        print(print_score(pscore,cscore,ties))
        
        print("--------------------------")
    print(print_score(pscore,cscore,ties))

# I love you for playing this xoxo don't fail me :)

rps()