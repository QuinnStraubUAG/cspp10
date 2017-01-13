#me and nickolus did this together
list_of_num = []
user = 6
while user != "exit":
    user = (input("Put in a command: "))

    if user == "clear" or user == "Clear":
        list_of_num = []
    elif user == "print" or user == "Print":
        print (list_of_num)
    elif user == "length" or user == "Length":
        print (len(list_of_num))
    elif user == "exit" or user == "Exit":
        print("Thanks for playing :) ")
    elif user == "sum" or user == "Sum":
        result = 0
        for x in list_of_num:
            result = result + x
        print (result)
    else:
        (list_of_num.append(int(user)))
        