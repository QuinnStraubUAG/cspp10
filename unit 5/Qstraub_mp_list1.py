#Nickolas and quinn did this
list = []
user = 2
while user != 0:
    user = input("Put in a number : ")
    user = int(user)
    if user > 0:
        print (user)
        list.append(user)
        print (list)
    elif user < 0:
        user = user - user - user
        list.remove(user)
        print (list)
    else:
        print ("Thx for doing stuff")
      
    
    