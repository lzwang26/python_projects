import random

# Card deck and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {str(i): i for i in range(2, 11)}
values.update({'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11})


# Card and Deck classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Game logic
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play(self):
        print("Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        self.show_hands(hide_dealer=True)

        # Player's turn
        while self.player_hand.value < 21:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                self.show_hands(hide_dealer=True)
            else:
                break

        # Dealer's turn
        if self.player_hand.value <= 21:
            while self.dealer_hand.value < 17:
                self.dealer_hand.add_card(self.deck.deal_card())

        self.show_hands()
        self.show_result()

    def show_hands(self, hide_dealer=False):
        print("\nYour hand:")
        for card in self.player_hand.cards:
            print(card)
        print(f"Total value: {self.player_hand.value}")

        print("\nDealer's hand:")
        if hide_dealer:
            print(self.dealer_hand.cards[0])
            print("<Hidden card>")
        else:
            for card in self.dealer_hand.cards:
                print(card)
            print(f"Total value: {self.dealer_hand.value}")

    def show_result(self):
        if self.player_hand.value > 21:
            print("You busted! Dealer wins.")
        elif self.dealer_hand.value > 21 or self.player_hand.value > self.dealer_hand.value:
            print("You win!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("Dealer wins.")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    while True:
        game = BlackjackGame()
        game.play()
        if input("Play again? (y/n): ").lower() != 'y':
            break
