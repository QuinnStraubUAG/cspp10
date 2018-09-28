# from pprint import pprint
thing = {
    
}
what_is_to_be_done = input("What would u like to do? (Lower case plz) ")
def contin():
    contin = input("What would u like to do? (Lower case plz) ")
    if contin == "remove":
        print("Yes remove more")
        return "remove"
    elif contin == "exit":
        print("Ok lets stop")
        return "exit"
    elif contin == "add":
        print("Yes add more")
        return "add"
    else:
        print("You broke it")
    
def diction_add(thing):
    while what_is_to_be_done != "exit":
        if what_is_to_be_done == "add":
            key_add = input("What do you want the key to be? ")
            input_add = input("What do you want {} to be ".format(key_add))
            print (key_add)
            print (input_add)
            if key_add in thing:
                print("You can put in the same thing twice")
            else:
                thing[key_add] = input_add
                print (thing)
            contin()
            break
def diction_remove(thing):
    key_remove = input("What would you like to remove (That is a key) ")
    if key_remove in thing:
        del thing[key_remove]
    else:
        print("That isn't in the dictionary")
while what_is_to_be_done != "exit" or contin() != "exit":
    if what_is_to_be_done == "add" or contin() == "add":
        diction_add(thing)
        what_is_to_be_done = 0
    elif what_is_to_be_done == "remove" or contin() == "remove":
        diction_remove(thing)
        what_is_to_be_done = 0
    else:
        print ("Done")
   