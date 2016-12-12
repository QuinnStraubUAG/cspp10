number = input(" Type a equation (No spaces plz) :")
num = int(number[0])
num_2 = int(number[2])

if number[1] == "+":
    print("The result is " + str(num + num_2))
elif number[1] == "-":
     print("The result is " + str(num - num_2))
elif number[1] == "*":
    print("The result is " + str(num * num_2))
elif number[1] == "/": 
    print("The result is " + str(num / num_2))
elif number[1] == "%":
    print("The result is " + str(num % num_2))
else:
    print ("Didn't input corecty")





# if number[1] == "+":
#     number = int(number[0])
#     number = int(number[2])
#     print(number[0] + number[2])
# elif number[1] == "-":
#     number = int(number[0])
#     number = int(number[2])
#     print (number[0] - number[2])
# elif number[1] == "*":
#     number = int(number[0])
#     number = int(number[2])
#     print (number[0] * number[2])
# elif number[1] == "/":
#     number = int(number[0])
#     number = int(number[2])
#     print (number[0] / number[2])
# elif number[1] == "%":
#   number = int(number[0])
#   number = int(number[2])
#   print (number[0] % number[2])
# else:
#  print ("Didn't input corecty")
# number = input(" Type a equation (No spaces plz) : ")
# number = int(number)
# print (number)
