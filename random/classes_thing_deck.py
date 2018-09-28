import random

class Card(object):
    #constructor - save data into isintance variables to be used later
    def __init__(self,suit,name,value):
        self.suit = suit
        self.name = name
        self.value = value
        
        
    def __str__(self):
        return "{} of {} (value={})".format(self.name,self.suit,self.value)
        
        
# c = Card("Hearts","King","13")
# print(c)

class Deck(object):
    #constructor
    def __init__(self):
        suits = ['Red','Yellow','Green','Blue']
        names = ["Zero",'One','Two','Three','Four','Five',
            'Six','Seven','Eight','Nine','Draw_2']
        values = [0,1,2,3,4,5,6,7,8,9,2000]
    
        self.cards = []
    
        #go through all the suits
        for suit in suits:
            #go through indexes for both names+values
            for index in range(len(names)):
                c = Card(suit,names[index],values[index])
                self.cards.append(c)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
d = Deck()
d.shuffle()
matched = 0
player_hand = []
opponent_hand = []
for x in range(7):
    player_hand.append(d.deal())
for x in range(7):
    opponent_hand.append(d.deal())
def print_player_hand(player_hand):
    for i in range(len(player_hand)):
        print ("{}: {}".format(i,player_hand[i]))
for i in range(len(player_hand)):
    print ("{}: {}".format(i,player_hand[i]))
deck = d.deal()
while (len(player_hand) != 0):
    print("Deck: {}".format(deck))
    choice = input("That matchs the color or number ")
    choice = int(choice)
    card_num = choice
    choice == player_hand[card_num]
    print ("You pulled out this card {} ".format(player_hand[choice]))
    deck_try = player_hand[choice]
    player_hand.remove(deck_try) 
    if deck.suit == "Red" and deck_try.suit == "Red":
        print ("You matched the color think you can do it again (Probably Not )")
        matched = 1
    elif deck.suit == "Yellow" and deck_try.suit == "Yellow":
        print ("You matched the color think you can do it again (Probably Not )")
        matched = 1
    elif deck.suit == "Blue" and deck_try.suit == "Blue":
        print ("You matched the color think you can do it again (Probably Not )")
        matched = 1
    elif deck.suit == "Green" and deck_try.suit == "Green":
        print ("You matched the color think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Zero" and deck_try.name == "Zero":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "One" and deck_try.name == "One":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Two" and deck_try.name == "Two":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Three" and deck_try.name == "Three":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Four" and deck_try.name == "Four":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Five" and deck_try.name == "Five":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Six" and deck_try.name == "Six":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Seven" and deck_try.name == "Seven":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Eight" and deck_try.name == "Eight":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Nine" and deck_try.name == "Nine":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1
    elif deck.name == "Draw_2" and deck_try.name == "Draw_2":
        print ("You matched the number think you can do it again (Probably Not )")
        matched = 1    
    else:
        print ("It didn't work")
        matched = 0
    if matched == 1:
        deck = deck_try
        print_player_hand(player_hand)
    else:
        print("Things didn't matched try again")
        print ("Heres Two cards to help you out")
        for x in range(2):
            player_hand.append(d.deal())
        player_hand.append(deck_try)
        print_player_hand(player_hand)
    if (len(player_hand) == 0):
        print ("You won the game of Uno I'm so proud")