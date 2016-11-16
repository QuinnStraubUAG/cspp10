import random

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
        
    print (AI)

        
        
get_comp_move()