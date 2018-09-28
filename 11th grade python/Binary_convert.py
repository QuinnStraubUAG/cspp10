lenth = 0
ones = []
binary_dec = 0
binary_begins = 0
user_bits = input("How many bits do you wanna use? ")
user_bits = int(user_bits)
ajust = user_bits + 1
for user_bits in range(user_bits):
    binary_begins = binary_begins + 1
binary_begins = 2**user_bits
binary_begins = binary_begins * 2 - 1
user_bits = user_bits + 1
print ("Maxuim number with {} bits is {}".format(user_bits,binary_begins))
user_num = input("What number do you wanna make b0ss? ")
conteant_dec = 0
user_num = int(user_num)
if user_num > binary_begins:
    print ("Thats not a thing you can do with {} bits".format(user_bits))
    chance = 0
else:
    print ("You made {} with {} bits good job bro".format(user_num,user_bits))
    chance = 1

if chance == 1:
    conteant = user_bits
    while conteant_dec != user_num or lenth != conteant - 1:
        lenth = len(ones) 
        lenth = int(lenth)
        user_bits = user_bits - 1
        test_b = 2**user_bits
        binary_dec = 0
        binary_dec = binary_dec + test_b
        if conteant_dec > user_num:
            binary_dec = binary_dec - binary_dec
            ones.append((0))
        else:
            conteant_dec = conteant_dec + binary_dec
            if conteant_dec > user_num:
                ones.append(0)
                conteant_dec = conteant_dec - test_b
            else:
                binary_dec = binary_dec - test_b
                ones.append(1)
    makeitastring = ''.join(map(str, ones))
    print ("It looks like this in binary {}".format(makeitastring))
    