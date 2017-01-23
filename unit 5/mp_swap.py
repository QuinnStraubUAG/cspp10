
def swap(original, index1, index2):
    for x in range(len(original)):
        if original[x] == index1:
            original[x] = index2
        elif original[x] == index2:
            original[x] = index1
            
original = [1,2,1,3,5,1,99,8008,99,720,1,0,99]
swap(original,1,99)
print (original)