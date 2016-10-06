number = input(" Type a equation (No spaces plz) :")
if number[1] == "+":
    number = int(number)
    print(number[0] + number[3])
elif number[1] == "-":
    number = int(number)
    print (number[0] - number[3])
elif number[1] == "*":
    number = int(number)
    print (number[0] * number[3])
elif number[1] == "/":
    number = int(number)
    print (number[0] / number[3])
elif number[1] == "%":
  number = int(number)
  print (number[0] % number[3])
else:
  print ("Didn't input corecty")
# number = input(" Type a equation (No spaces plz) : ")
# number = int(number)
# print (number)
