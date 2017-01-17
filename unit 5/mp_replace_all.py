# def first_try():
#     original = [1,2,3,69,8008,420,42,87,4,69]
#     print (original)
#     print ("We will take out 69")
#     original.remove(69)
#     original.insert(3,"ha XDDDDDDDDDDDDDDDD how funny and main stream")
#     original.remove(69)
#     original.insert(9,"ha XDDDDDDDDDDDDDDDD how funny and main stream")
#     print(original)

# def one_with_var():
#     to_replace = 69
#     original = [1,2,3,to_replace,8008,420,42,87,4,to_replace]
#     print (original)
#     print ("We will take out 69")
#     to_replace = "ha XDDDDDDDDDDDDDDDD how funny and main stream"
#     original = [1,2,3,to_replace,8008,420,42,87,4,to_replace]
#     print(original)

# print("I will run 2 functions that do the same thing")
# first_try()
# one_with_var()



def MP_4():
    to_replace = 69
    a = [to_replace,720,42]
    print (a)
    replace_with = "ha XDDDDDDDDDDDDDDDD how funny and main stream"
    a.insert(0,replace_with)
    a.remove(to_replace)
    print(a)
    
MP_4()

# names = []
# choice_of_names = 0
# while choice_of_names != "Done":
#     choice_of_names = input("Enter a name: ")
#     names.insert(0,choice_of_names)
    
#     print(names)
# names.remove("Done")