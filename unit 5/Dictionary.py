# from pprint import pprint
thing = {
    
}
what_is_to_be_done = input("What would u like to do? (Lower case plz) ")
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
            else:
                print("")
while what_is_to_be_done != "exit":
    if what_is_to_be_done == "add":
        diction_add(thing)
    else:
        print ("Done")
   