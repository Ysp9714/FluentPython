import collections
from decorater.time_func import *
import doctest


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
deck = FrenchDeck()
len(deck)

deck[:3] # 앞에서부터 3개
deck[1::3] # 1에서 시작해서 인덱스번호 3씩 증가

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    # list.index(x) > 위치 반환
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)