class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.suit}{self.rank}'


class Deck:

    def __init__(self):
        from itertools import product

        self.deck = [Card(i, j) for i, j in
                     product(['♣', '♢', '♡', '♠'],
                             ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])]

    def shuffle(self):

        if len(self.deck) == 52:
            self.deck.reverse()
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def __repr__(self):
        return f'Карт в колоде: {len(self.deck)}'

    def deal(self):

        if self.deck:
            return self.deck.pop(-1)
        else:
            raise ValueError('Все карты разыграны')
