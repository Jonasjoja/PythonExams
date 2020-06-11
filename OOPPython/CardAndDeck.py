from random import shuffle

class Card():

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"



class Deck():
    
    def __init__(self):
        #Lists of suits and values.
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value,suit) for suit in suits for value in values] #List comprehension to create a deck


    def __repr__(self): #Repr method to represent how many cards are left in the deck.
        return f"Deck of {self.count()} cards"

    

    def count(self): #Instance method to return amount of cards left
        return len(self.cards)

    def _deal(self, num):
        count = self.count() #Check number of cards in deck
        actual = min([count,num]) #Cant remove 5 cards if there's only 3 in deck. So uses whichever value is lowest.
        if count == 0: #Handles if 0 cards in deck
            raise ValueError("All cards have been dealt")

        cards = self.cards[-actual:] #Slicing, will go from -index til : which is the end.
        self.cards = self.cards[:-actual] #from beginning to -actual
        return cards #returns what has been taken off/has been dealt

    def deal_card(self): #Always deals 1 card
        return self._deal(1)[0]

    def deal_hand(self,handSize): #deals a hand of specified size.
        return self._deal(handSize)

    def shuffle(self): #uses imported shuffle method to shuffle cards

        if self.count() < 52: #will only shuffle full decks.
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self #Just convention, if wanted to save to a variable at some point


d = Deck() #Create a deck instance
d.shuffle() #shuffling the deck
print(d) #prints the now shuffled deck
card = d.deal_card()
print(card) #prints the dealt card
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards) #prints empty list cause the card deck is now empty
card2 = d.deal_card()