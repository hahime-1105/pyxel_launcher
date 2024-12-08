import pyxel
from enum import Enum, auto
from random import shuffle
import numpy as np


class Suit(Enum):
    spade = '♠'
    heart = '♡'
    dia = '♢'
    club = '♣'

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'Suit.{self.name}'


class Role(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_STRAIGHT_FLUSH = auto()


class Number(Enum):
    ace = (1, 'A')
    two = (2, '2')
    three = (3, '3')
    four = (4, '4')
    five = (5, '5')
    six = (6, '6')
    seven = (7, '7')
    eight = (8, '8')
    nine = (9, '9')
    ten = (10, '10')
    jack = (11, 'J')
    queen = (12, 'Q')
    king = (13, 'K')

    def __init__(self, val, string):
        self.val = val
        self.string = string

    def __int__(self):
        return self.val

    def __str__(self):
        return self.string

    def __repr__(self):
        return f'Number.{self.name}'


class Card:

    def __init__(self, suit, number):
        if not (isinstance(suit, Suit) and isinstance(number, Number)):
            raise ValueError  # Enumでなければエラーを返す
        self.suit = suit
        self.number = number

    def __str__(self):
        return str(self.suit) + str(self.number)

    def __repr__(self):
        return f'Card({self.__str__()})'


class Deck(list):
    def __init__(self):
        super().__init__(
            Card(suit, number) for suit in Suit for number in Number
        )

        self.shuffle()

    def shuffle(self):
        shuffle(self)

    def draw(self):
        return self.pop()


# 手札と役を保持
class Hand(Deck):
    def __init__(self, Deck, num):
        self.hand = []
        self.num = num
        for i in range(self.num):
            self.hand.append(Deck.draw())

    def sort(self):
        # 数字を昇順
        self.list = np.zeros(self.num, dtype=np.int8)
        for j in range(self.num):
            self.list[j] = self.hand[j].number.__int__()
        self.ind = np.argsort(self.list)
        self.tmp_hand = []
        for k in range(self.num):
            self.tmp_hand.append(self.hand[self.ind[k]])
        self.hand = self.tmp_hand

    def role(self):
        self.flush_flag = True
        self.str_flag = True
        self.pair_count1 = 0
        self.pair_cut = True
        self.pair_count2 = 0
        for l in range(self.num - 1):
            if not self.hand[l].suit.__str__() == self.hand[l + 1].suit.__str__():
                self.flush_flag = False
            if not self.hand[l].number.__int__() == (self.hand[l + 1].number.__int__() + 1) or (
                    self.hand[l].number.__int__() == 1 and self.hand[l + 1].number.__int__() == 10):
                self.str_flag = False
            if self.hand[l].number.__int__() == self.hand[l + 1].number.__int__():
                if self.pair_cut:
                    self.pair_count1 += 1
                else:
                    self.pair_count2 += 1
            elif not self.pair_count1 == 0:
                self.pair_cut = False
        print(self.flush_flag, self.str_flag, self.pair_count1, self.pair_count2)
        if self.flush_flag and self.str_flag and self.hand[0].number.__int__() == 1 and self.hand[
            1].number.__int__() == 10:
            return Role.ROYAL_STRAIGHT_FLUSH
        elif self.flush_flag and self.str_flag:
            return Role.STRAIGHT_FLUSH
        elif self.pair_count1 == 3:
            return Role.FOUR_OF_A_KIND
        elif (self.pair_count1 + self.pair_count2) == 3:
            return Role.FULL_HOUSE
        elif self.flush_flag:
            return Role.FLUSH
        elif self.str_flag:
            return Role.STRAIGHT
        elif self.pair_count1 == 2:
            return Role.THREE_OF_A_KIND
        elif self.pair_count1 == 1 and self.pair_count2 == 1:
            return Role.TWO_PAIR
        elif self.pair_count1 == 1:
            return Role.ONE_PAIR
        else:
            return Role.HIGH_CARD


if __name__ == '__main__':
    deck = Deck()
    playerhand = Hand(deck, 5)
    for j in range(5):
        print(playerhand.hand[j])
    playerhand.sort()
    print(playerhand.role())
