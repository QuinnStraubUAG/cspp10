import random
fails = 0
opponent = 1
opponent_hp = 200
player_hp = 150
p_damage = 0
teacher = input("Do you want a tutorial [Y or N](make sure it is in CAPS): ")
if teacher == "Y":
    # print("I will type a thing later")
    print("Ok this is how you play you each have a certain amount of helth and 4 different attacks which do different things")
    print ("so ether selet an attack or type the number for the attack and i right after (lower case no space) to get the info on the attack")
else:
    print("Ok lets start")
print("A wild eevee has appered")
print ("Go Persian(Alolan)")
while opponent != 0 and opponent != 2:
    print("Eevee has {} Health".format(opponent_hp))
    print("You have {} Health".format(player_hp))
    print("Your attacks: Feint attack(1),Night slash(2),Power gem(3),Dark pulse(4)")
    Player_turn = input("Type what attack you would like to use (Type it exactly as you see it ")
    info = 5
    while info != 0:
        if Player_turn == "1i":
            info = 1 
        elif Player_turn == "2i":
            info = 2
        elif Player_turn == "3i":
            info = 3
        elif Player_turn == "4i":
            info = 4
        else:
            info = 0
        if info == 1:
            print("Feint attack this move does 20 damage and never misses")
            print("Your attacks: Feint attack(1),Night slash(2),Power gem(3),Dark pulse(4)")
            Player_turn = input("Type what attack you would like to use (Type it exactly as you see it ")
        elif info == 2:
            print("Night slash this move does 35 damage and has a highier chance in critical hits (critical hits not yet implmented)")
            print("Your attacks: Feint attack(1),Night slash(2),Power gem(3),Dark pulse(4)")
            Player_turn = input("Type what attack you would like to use (Type it exactly as you see it ")
        elif info == 3:
            print("Power gem this just does 50 damage")
            print("Your attacks: Feint attack(1),Night slash(2),Power gem(3),Dark pulse(4)")
            Player_turn = input("Type what attack you would like to use (Type it exactly as you see it ")    
        elif info == 4:
            print("Dark pulse this does 40 damage and has a 20% chance to make the target flinch (Flinching not yet implmented :( )")
            print("Your attacks: Feint attack(1),Night slash(2),Power gem(3),Dark pulse(4)")
            Player_turn = input("Type what attack you would like to use (Type it exactly as you see it ")
        else:
            fails = fails + 1
    if Player_turn == "Feint attack" or Player_turn == "1":
        print("Used Feint attack")
        p_attack = 1
    elif Player_turn == "Night slash" or Player_turn == "2":
        print("Used Night slash")
        p_attack = 2
    elif Player_turn == "Power gem" or Player_turn == "3":
        print ("Used Power gem")
        p_attack = 3
    elif Player_turn == "Dark pulse" or Player_turn == "4":
        print("Used Dark pulse")
        p_attack = 4
    elif Player_turn == "1i":
        info = 1 
    elif Player_turn == "2i":
        info = 2
    elif Player_turn == "3i":
        info = 3
    elif Player_turn == "4i":
        info = 4
    else:
        print("You typed somthing wrong and now it's broken good job")
        break
    damage = 0
    miss_chance = int((random.randint(1,100)))
    miss_chance_o = int((random.randint(1,100)))
    if p_attack == 1:
        damage = 20
        print("You did {} damage".format(damage))
        #never misses
    elif p_attack == 2 and miss_chance != 100:
        damage = 35
        print("You did {} damage".format(damage))
        #has a higher chance of critical hits
    elif p_attack == 3 and miss_chance != 100:
        damage = 50
        print("You did {} damage".format(damage))
    elif p_attack == 4 and miss_chance != 100:
        damage = 40
        print("You did {} damage".format(damage))
    elif p_attack == 2 and miss_chance == 100:
        print ("You missed")
        #has a higher chance of critical hits
    elif p_attack == 3 and miss_chance == 100:
        print ("You missed")
    elif p_attack == 4 and miss_chance == 100:
        print ("You missed")
        #Makes the target flinch
    else:
        print("You broke it")
        break
    opponent_hp = opponent_hp - damage
    if opponent_hp <= 0:
        print("You did it Eevee has been defeated")
        opponent = 0
        break
    else:
        fails = fails + 1
        damage = 0
    o_attack = int((random.randint(1,4)))
    if o_attack == 1:
        print ("Eevee used Swift it did 35 damage")
        # Swift
        #Never misses
        p_damage = 35
    elif o_attack == 2 and miss_chance_o != 100:
        print ("Eevee used Bite it did 30 damage")
        #bite
        #30% chance to finch
        p_damage = 30
    elif o_attack == 3 and miss_chance_o != 100:
        print ("Eevee used Take Down it did 60 damage it hurt it self with recoil damage")
        #Take down
        #Does 25% of the damage to it's self
        p_damage = 60
        damage = 15
        player_hp = player_hp - p_damage
    elif o_attack == 4 and miss_chance_o != 100:
        print ("Eevee used Double Edge it did 80 damage it hurt it self with recoil damage")
        #Double Edge
        #Does 1/3 of the dmage to its self
        p_damage = 80
        damage = 26
        player_hp = player_hp - p_damage
    elif o_attack == 2 and miss_chance_o == 100:
        print("Eevee used bite")
        print ("It missed")
    elif o_attack == 3 and miss_chance_o == 100:
        print("Eevee used Take down")
        print ("It missed")
    elif o_attack == 4 and miss_chance_o == 100:
        print("Eevee used double edge")
        print ("It missed")
    else:
        fails = fails + 1
    opponent_hp = opponent_hp - damage
    if player_hp <= 0:
        print("You are dead")
        print("Game Over yeahhhhh")
        break
    elif opponent_hp <= 0:
        print("You did it Eevee has been defeated")
        # print(opponent_hp)
        opponent = 0
    else:
        fails = fails + 1