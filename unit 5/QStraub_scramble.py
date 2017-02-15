import random
word = "hello"
word_works = 0
scrambled_well = 1
def scramble_word(word,scrambled_well):
    list_1 = []
    letter_check = word[0]
    letter_check_2 = word[-1]
    if len(word) == (1):
        print ("Stop_1")
    elif len(word) == (2):
        print("Stop_2")
    elif len(word) == (3):
        print("Stop_3")
    else:
        word_works = 1
    
    while word_works == 1 and scrambled_well == 1:
        middle_letters = word[1:-1]
        print (middle_letters)
        list_1 = list(middle_letters)
        print (list_1)
        random.shuffle(list_1)
        print (list_1)
        final = ''.join(list_1)
        if final == "ell":
            scrambled_well = 1
        else:
            scrambled_well = 0
    
    print (final)
    final = (letter_check + final + letter_check_2)
    return (final)
    
    
    

scramble_word(word,scrambled_well)
#I would first get a word
#Next I would make some varibles that would that the first and last letters
#Then I whould shuffle everything but the last letters
#Next I would check if they got shuffled with some len stuff
#Then stuff will work
# def scramble_phrase():
# scramble_word()
def scramble_phrase():
    print 
scramble_phrase()