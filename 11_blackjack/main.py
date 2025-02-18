import art
import random

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if if_play == 'y':
        print(art.logo)
        your_cards = random.sample(cards, 2)
        sum_your_cards = sum(your_cards)
        print("Your cards:", your_cards, "current score:", sum_your_cards)
        pc_cards = random.sample(cards, 1)
        print("Computer's first card:", pc_cards[0])
        get_another = input("Type 'y' to get another card, type 'n' to pass: ")
        while get_another == 'y':
            your_cards.append(random.randint(1, 10))
            print(your_cards)
            sum_your_cards = sum(your_cards)
            sum_pc_cards = sum(pc_cards)
            print("Your cards:", your_cards, "current score:", sum_your_cards)
            if (sum_your_cards  <= 21) and (sum_pc_cards <= 21):
                pc_cards.append(random.randint(1, 10))
                print("Computer's cards:", pc_cards, "current score:", sum_pc_cards)
                get_another = input("Type 'y' to get another card, type 'n' to pass: ")
            elif sum_your_cards > 21:
                print("Your final hand:", your_cards, "final score:", sum_your_cards)
                print("Computer's final hand:", pc_cards, "final score:", sum_pc_cards)
                print("You went over. You lose")
                blackjack()
            elif sum_pc_cards > 21:
                print("Your final hand:", your_cards, "final score:", sum_your_cards)
                print("Computer's final hand:", pc_cards, "final score:", sum_pc_cards)
                print("Computer went over. You win")
        pc_cards.append(random.randint(1, 10))
        sum_your_cards = sum(your_cards)
        sum_pc_cards = sum(pc_cards)
        print("Your final hand:", your_cards, "final score:", sum_your_cards)
        print("Computer's final hand:", pc_cards, "final score:", sum_pc_cards)
        if sum_your_cards > sum_pc_cards:
            print("You win")
        else:
            print("You lose")
        blackjack()
    else:
        print("You don't want to play.")



blackjack()