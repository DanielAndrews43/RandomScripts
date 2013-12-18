class FullDeck():
    '''
    Returns a full 52 card deck
    '''
    def __init__(self):
        self.names = ('Ace','One','Two','Three','Four','Five','Six','Seven','Eight',
                'Nine','Ten','Jack','Queen','King')     
        self.suits = ('Hearts','Spades','Clubs','Diamonds')
        self.createDeck()
        
    def createDeck(self):
        currentDeck = []
        for it1 in self.names:
            for it2 in self.suits:
                currentDeck.append(it1 + ' of ' + it2)
        self.deck = currentDeck
    
    def __str__(self):
        return str(self.deck)        
class Hand():
    '''
    takes a deck and randomly takes cards from it.
    Removes all used cards
    '''
    def __init__(self, n, deck):
        '''
        Takes amount of cards in hand, int n
        Takes current deck, FullDeck deck
        '''
        self.hand = self.createHand(n,deck)
        
    def createHand(self,n,deck):
        from random import random
        '''
        creates a hand from the deck
        '''
        currHand = []
        currCard = ''
        for i in range(n):
            currCard = deck[int(random()*len(deck))]
            currHand.append(currCard)
            deck.remove(currCard)
        return currHand
    
    def __str__(self):
        return str(self.hand)
    