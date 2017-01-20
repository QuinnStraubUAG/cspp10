#Me and Nickulus did this

def extend(original,b_list):
    for c in b_list:
        original.append(c)
   
original = [1,2,3]
b_list = [4,5,6]
extend(original,b_list)
print (original)