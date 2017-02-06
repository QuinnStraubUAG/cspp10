import random
word = "hello"
word_works = 0
def scramble_word(word):
    list_1 = []
    # letter_check = word[1]
    # letter_check_2 = word[-2]
    # print (word[1:-1])
    if len(word) == (1):
        print ("Stop_1")
    elif len(word) == (2):
        print("Stop_2")
    elif len(word) == (3):
        print("Stop_3")
    else:
        word_works = 1
    
    if word_works == 1:
        middle_letters = word[1:-1]
        print (middle_letters)
        list_1 = list(middle_letters)
        print (list_1)
        random.shuffle(list_1)
        print (list_1)
    else:
        print ("NO")
    final = '+'.join(list_1)
    print (final)
    
    final.index(+[, 1[, 3]])
    

scramble_word(word)
#I would first get a word
#Next I would make some varibles that would that the first and last letters
#Then I whould shuffle everything but the last letters
#Next I would check if they got shuffled with some len stuff
#Then stuff will work
# def scramble_phrase():
# scramble_word()
# scramble_phrase()