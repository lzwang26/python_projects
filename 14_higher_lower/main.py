import art
from game_data import data
import random
print(art.logo)

def select_second_option(tot_ind, fir_ind):
    available_items = [num for num in tot_ind if num != fir_ind]
    sec_ind = available_items[random.sample(tot_ind, 1)[0]]
    return sec_ind

def print_info(a, b):
    """Format the account data into printable format"""
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(art.vs)
    print(f"Against B:, {b["name"]}, a {b["description"]}, from {b["country"]}")

def game():
    total_indices = list(range(0, len(data) - 1))
    answer_index = total_indices[random.sample(total_indices, 1)[0]]
    game_over = False
    score = 0
    while not game_over:
        first_option = data[total_indices[answer_index]]
        second_index = select_second_option(total_indices, answer_index)
        second_option = data[second_index]
        print_info(first_option, second_option)
        selection = input("Who has more followers? Type 'A' or 'B': ").lower()
        if first_option["follower_count"] > second_option["follower_count"]:
            answer = "a"
        else:
            answer = "b"

        if selection == answer:
            score += 1
            print("You're right! Current score:", score)
            if selection == "b":
                answer_index = second_index
        else:
            game_over = True
            print("Sorry, that's wrong. Final score:", score)
        print(len(total_indices))
game()