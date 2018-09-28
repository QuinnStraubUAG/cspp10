import random
startup = 100
health = 100
health = int(health)
while startup != 0:
    def battle():
        rng = 0
        print ("An enemy is in the room and does 20 damage")
        attack = input("Whould you like to attack, defend, run (You can type A,D, or R Just remember there is a chance for failure ")
        print (attack)
        if attack == "A" or attack == "a":
            attack = 1
            print (attack)
        else:
            attack = 0
        rng = (int(random.randint(1,10)))
        p_damage = 0
        if attack == 1 and rng == 1:
            print ("You missed and got hit for 30 damage")
            print (rng)
            p_damage = 30
            p_damage = int(p_damage)
        elif attack == 1 and rng == 2:
            print ("You missed and you got hit for 25 damage")
            print (rng)
            p_damage = 25
            p_damage = int(p_damage)
        elif attack == 1 and rng == 3:
            print ("You missed and you got hit for 20 damage")
            print (rng)
            p_damage = 20
            p_damage = int(p_damage)
        elif attack == 1 and rng == 4:
            print ("You missed and you got hit for 15 damage")
            print (rng)
            p_damage = 15
            p_damage = int(p_damage)
        elif attack == 1 and rng == 5:
            print ("You missed but dogged an incoming attack")
            print (rng)
        elif attack == 1 and rng == 6:
            print ("You landed a hit for 10 damage ")
            print (rng)
            o_damage = 10
        elif attack == 1 and rng == 7:
            print ("You landed a hit for 15 damage ")
            print (rng)
            o_damage = 15
        elif attack == 1 and rng == 8:
            print ("You landed a hit for 20 damage ")
            print (rng)
            o_damage = 20
        elif attack == 1 and rng == 9:
            print ("You landed a hit for 25 damage ")
            print (rng)
            o_damage = 25
        elif attack == 1 and rng == 10:
            print ("You landed a hit for 30 damage ")
            print (rng)
            o_damage = 30
        else:
            rng = 0
            
        return (p_damage)
    damage_after = battle()
    damage_after = int(damage_after)
    health = health - damage_after
    print (health)