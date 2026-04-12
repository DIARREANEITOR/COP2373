import random


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["n/a", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit, self.rank = suit, rank

    def __str__(self):
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in range(4) for r in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()


def get_hand(deck):
    return [deck.pop_card() for _ in range(5)]


def replace_cards(hand, deck):
    print("\nYour hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")

    choices = input("\nEnter card numbers to replace ( 1,2,3,4,5): ")
    if choices:
        indices = [int(x.strip()) - 1 for x in choices.split(",")]
        for idx in indices:
            if 0 <= idx < 5:
                hand[idx] = deck.pop_card()
    return hand


def main():
    deck = Deck()
    deck.shuffle()

    hand = get_hand(deck)
    hand = replace_cards(hand, deck)

    print("\nFinal hand:")
    for card in hand:
        print(card)


if __name__ == "__main__":
    main()