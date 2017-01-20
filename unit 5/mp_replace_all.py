# #Me and Nickulus did this

    
def replace_all(original, to_replace, replace_with):
    for x in range(len(original)):
        if original[x] == to_replace:
            original[x] = replace_with
            
original = [1,2,1,3,5,1]
replace_all(original,1,99)
print (original)
            