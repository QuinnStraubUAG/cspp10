contin = 1
x = -1
user_input = 0
name_list = []
# last_name_list = []
# grade_list = []
while contin == 1:
    user_input = user_input + 1
    first_name = input("Put in your first name plz: ")
    last_name = input("Put in your last name plz: ")
    grade = input("What grade are you in: ")
    print ("So your first name is {} and your last name is {} and your grade is {} kool".format(first_name,last_name,grade))
    contin_y_n = input("Do you want to keep going yes or no:  ")
    name_list.append(first_name)
    name_list.append(last_name)
    name_list.append(grade)
    if contin_y_n == "Yes" or contin_y_n == "yes" or contin_y_n == "Y" or contin_y_n == "y":
        contin = 1
    else:
        print (name_list)
        for w in range(user_input):
            print ("So your first name is " + name_list[x+1] + " and your last name is " + name_list[x+2] + " and your grade is " + name_list[x+3] + " kool")
            x = x + 3
        contin = 0
        
