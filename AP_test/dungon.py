import random 
#print ("You used the w,a,s,d {} times, you typed the full word {} times".format(short_key_use,full_key_use))
health = 100 
# My friend helped me design and fix the battle system
def battle(p_health):
    o_damage = 0
    p_damage = 0
    opponent_hp = 100
    while opponent_hp > 0:
        print ("The opponent hp is")
        print (opponent_hp)
        print ("The player hp is")
        print (p_health)
        rng = 0
        print ("An enemy is in the room ")
        attack = input("Press a too attack ")
        if attack == "A" or attack == "a":
            attack = 1
        else:
            attack = 0
        rng = (int(random.randint(1,10)))
        p_damage = 0
        if attack == 1 and rng == 1:
            print ("You missed and got hit for 30 damage")
            p_damage = 30
            p_damage = int(p_damage)
        elif attack == 1 and rng == 2:
            print ("You missed and you got hit for 25 damage")
            p_damage = 25
            p_damage = int(p_damage)
        elif attack == 1 and rng == 3:
            print ("You missed and you got hit for 20 damage")
            p_damage = 20
            p_damage = int(p_damage)
        elif attack == 1 and rng == 4:
            print ("You missed and you got hit for 15 damage")
            p_damage = 15
            p_damage = int(p_damage)
        elif attack == 1 and rng == 5:
            print ("You missed but dogged an incoming attack")
            o_damage = 0
        elif attack == 1 and rng == 6:
            print ("You landed a hit for 10 damage ")
            o_damage = 10
        elif attack == 1 and rng == 7:
            print ("You landed a hit for 15 damage ")
            o_damage = 15
        elif attack == 1 and rng == 8:
            print ("You landed a hit for 20 damage ")
            o_damage = 20
        elif attack == 1 and rng == 9:
            print ("You landed a hit for 25 damage ")
            o_damage = 25
        elif attack == 1 and rng == 10:
            print ("You landed a hit for 30 damage ")
            o_damage = 30
        else:
            rng = 0
        opponent_hp = opponent_hp - o_damage
        p_health = p_health - p_damage
        if opponent_hp < 1:
            print ("The enemies has been slain")
            return 1
        elif p_health < 1:
            print ("You are a dead") 
            return 0
def boss_battle(p_health,item_2,item_3,item_4,item_bow):
    o_damage = 0
    p_damage = 0
    opponent_hp = 300
    if item_2 == 1:
        print ("The power of your Pendant of Courage droped the bosses helth by 50 hp")
        opponent_hp = opponent_hp - 50
    if item_3 == 1:
        print ("The power of your Pendant of Power droped the bosses helth by 50 hp")
        opponent_hp = opponent_hp - 50
    if item_4 == 1:
        print ("The power of your Pendant of Wisdom droped the bosses helth by 50 hp")
        opponent_hp = opponent_hp - 50
    if item_bow == 1:
        shot = input("Would you like to get a early shot off with your bow Y/N: ")
        if shot == "Y" or shot == "y":
            shot = 1
            print ("Your ancient bow did 10 damage")
            opponent_hp = opponent_hp - 10
        elif shot == "N" or shot == "n":
            shot = 0
        else:
            shot = 0
    print ("A boss is in the room there is no escape now ")
    while opponent_hp > 0:
        print ("The opponent hp is")
        print (opponent_hp)
        print ("The player hp is")
        print (p_health)
        rng = 0
        attack = input("Press a too attack ")
        if attack == "A" or attack == "a":
            attack = 1
        else:
            attack = 0
        rng = (int(random.randint(1,10)))
        p_damage = 0
        if attack == 1 and rng == 1:
            print ("You missed and got hit for 30 damage")
            p_damage = 30
            p_damage = int(p_damage)
        elif attack == 1 and rng == 2:
            print ("You missed and you got hit for 25 damage")
            p_damage = 25
            p_damage = int(p_damage)
        elif attack == 1 and rng == 3:
            print ("You missed and you got hit for 20 damage")
            p_damage = 20
            p_damage = int(p_damage)
        elif attack == 1 and rng == 4:
            print ("You missed and you got hit for 15 damage")
            p_damage = 15
            p_damage = int(p_damage)
        elif attack == 1 and rng == 5:
            print ("You missed but dogged an incoming attack")
            print (rng)
            o_damage = 0
        elif attack == 1 and rng == 6:
            print ("You landed a hit for 10 damage ")
            o_damage = 10
        elif attack == 1 and rng == 7:
            print ("You landed a hit for 15 damage ")
            o_damage = 15
        elif attack == 1 and rng == 8:
            print ("You landed a hit for 20 damage ")
            o_damage = 20
        elif attack == 1 and rng == 9:
            print ("You landed a hit for 25 damage ")
            o_damage = 25
        elif attack == 1 and rng == 10:
            print ("You landed a hit for 30 damage ")
            o_damage = 30
        else:
            rng = 0
        opponent_hp = opponent_hp - o_damage
        p_health = p_health - p_damage
        if opponent_hp < 1:
            print ("The enemies has been slain")
            return 1
        elif p_health < 1:
            print ("U a deaded")  
            return 0
room = 1
short_key_use = 0
full_key_use = 0
room = 1
enemies_2 = 1
where_you_go = 2990
item_2 = 1
item_3 = 1
item_4 = 1
item_7 = 1
item_2_u = 0
item_3_u = 0
item_4_u = 0
item_7_u = 0
key = 1
key_u = 0
while where_you_go != 3000:
    where_you_go = input("Where do you want to go type (w,a,s,d or left, right, foward, back) btw you can type info if you need  ")
    if where_you_go == "foward":
        where_you_go = "w"
        full_key_use = full_key_use + 1
    elif where_you_go == "W":
        where_you_go = "w"
        short_key_use = short_key_use + 1
    elif where_you_go == "back":
        where_you_go = "s"
        full_key_use = full_key_use + 1
    elif where_you_go == "S":
        where_you_go = "s"
        short_key_use = short_key_use + 1
    elif where_you_go == "left":
        where_you_go = "a"
        full_key_use = full_key_use + 1
    elif where_you_go == "A":
        where_you_go = "a"
        full_key_use = full_key_use + 1
    elif where_you_go == "right":
        where_you_go = "d"
        full_key_use = full_key_use + 1
    elif where_you_go == "D":
        where_you_go = "d"
        short_key_use = short_key_use + 1
    else:
        short_key_use = short_key_use + 1
    if where_you_go == "map" and room == 1:
        print("""                           --------------- -------------------
                           |             | |                 |
                           |                                 |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                            0                  |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |          |
                           |          | 
                           ------------
""")
    if where_you_go == "room":
        print (room)
    if where_you_go == "health":
        print (health)
    if where_you_go == "info":
        print ("It already says how to move you can type map to pull up a map telling you your location")
        #My Friend helped me design and fix the room system
    if where_you_go == "w" and room == 1:
        room = 2
        if enemies_2 == 1:
            win_lose = battle(health)
            win_lose = int(win_lose)
            if win_lose == 1:
                enemies_2 = 0
                print ("You healed after the battle")
            elif win_lose == 0:
                print ("I cri in my cri")
                break
        if item_2 == 1:
            print("You found the Pendant of Power")
            item_2 = 0
            item_2_u = 1
    if where_you_go == "d" and room == 2:                 
        room = 7
        if room == 7 and item_7 == 1:
            item_7 = 0
            item_7_u = 1
            print("You found the ancient bow")
            
    if where_you_go == "a" and room == 5:
        boss_door = input("Would you like to enter the boss door Y/N: ")
        if boss_door == "Y" or boss_door == "y":
            boss_door = 1
        else:
            boss_door = 0
        if boss_door == 1 and key_u == 1:
            room = 6
            boss_battle = boss_battle(health,item_2_u,item_3_u,item_4_u,item_7_u)
            boss_battle = int(boss_battle)
            if boss_battle == 1:
                print("You win you beat the boss")
                break
            elif boss_battle == 0:
                print ("The boss has taken you down")
                break
        elif boss_door == "N" or boss_door == "n":
            room = 5
        else:
            print ("You don't have the key")
            room = 5
    if where_you_go == "d" and room == 1:
        room = 3
        if item_3 == 1:
            print("You found the Pendant of Wisdom")
            item_3 = 0
            item_3_u = 1
    if where_you_go == "a" and room == 1:
        room = 5
        if item_4 == 1:
            print ("You found the Pendant of Courage")
            item_4 = 0
            item_4_u = 1
    if where_you_go == "s" and room == 1:
        room = 4
        if key == 1:
            print ("You found the key to the boss room")
            key = 0
            key_u = 1
    if where_you_go == "a" and room == 7:
        room = 2
    if where_you_go == "a" and room == 3:
        room = 1
    if where_you_go == "w" and room == 4:
        room = 1
    if where_you_go == "d" and room == 5:
        room = 1
    if where_you_go == "s" and room == 2:
        room = 1
    if where_you_go == "map" and room == 2:
        print("""                           --------------- -------------------
                           |             | |                 |
                           |     0                           |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                                               |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |          |
                           |          | 
                           ------------
    """)
    if where_you_go == "map" and room == 3:
        print("""                           --------------- -------------------
                           |             | |                 |
                           |                                 |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                                          0    |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |          |
                           |          | 
                           ------------
""")
    if where_you_go == "map" and room == 4:
        print("""                           --------------- -------------------
                           |             | |                 |
                           |                                 |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                                               |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |     0    |
                           |          | 
                           ------------
    """)
    if where_you_go == "map" and room == 5:
                print("""                           --------------- -------------------
                           |             | |                 |
                           |                                 |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                0                              |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |          |
                           |          | 
                           ------------
    """)
    if where_you_go == "map" and room == 7:
                print("""                           --------------- -------------------
                           |             | |                 |
                           |                        0        |
                           |             | |                 |
                           ----     ------ -------------------
   ----------- ----------- ----     --- ------------
   |         | |         | |          | |          |
   |                                               |
   |         | |         | |          | |          |
   ----------- ----------- ---    ----- ------------
                           ---    -----
                           |          |
                           |          |
                           |          | 
                           ------------
    """)