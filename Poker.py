

import random 
class Card (object):
  value_str = ('ace',2, 3, 4, 5, 6, 7, 8, 9, 10, 'king', 'jack', 'queen')

  suit = ('hearts', 'spades', 'diamond', 'clubs')
  def __init__ (self, value_str, suit):
    self.value_str = value_str
    self.suit = suit

  def  getSuit(self,suit):
    return self.suit

  def getValueStr(self,value_str):
        return self.value_str

  def getValue(self):
        if self.value_str == 'ace':
          value_str = 1
        elif self.value_str == 10:
           value_str = 'king'
        elif self.value_str == 10:
           value_str = 'queen'
        elif self.value_str == 10:
            value_str = 'jack'
        else:
            value_str = self.value_str
        return str(value_str) + self.suit
        
        return self.value
      
  def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.value_str[self.value_str],
                                   Card.suit[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

class deck:
  def __init__(self):
        self.cards = []
        for suit in range(4):
            for value_str in range(1, 14):
                self.cards.append(Card(suit, value_str))
  def reset(self):
       deck.__init__
  def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
def drawCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
class Hand(deck):
    def __init__(self, name=""):
       self.cards = []
       self.name = name
    def addToHand(self,card):
        self.cards.append(card)
    def emptyHand(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break   # break if out of cards
            card = self.pop()           # take the top card
            hand = hands[i % num_hands] # whose turn is next?
            hand.add(card)              # add the card to the hand
    def __str__(self):
            s = "Hand " + self.name
            if self.is_empty():
                  s = s + " is empty\n"
            else:
                   s = s + " contains\n"
            return s + deck.__str__(self)