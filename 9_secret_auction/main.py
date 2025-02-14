import art
print(art.logo)

def find_highest_bid(dictionary):
    highest_bid = 0
    highest_key = ""
    for key, value in dictionary.items():
        if value > highest_bid:
            highest_bid = value
            highest_key = key
    print(f"The winner is {highest_key} with a bid of {highest_bid}!")


game_over = False

bid_dict = {}
while not game_over:
    name = input("Name: ")
    amount = int(input("Amount: "))

    bid_dict[name] = amount

    game_over_input = input("Want to have a new bid? ").lower()
    if game_over_input == "no":
        game_over = True
        find_highest_bid(bid_dict)
    elif game_over_input == "yes":
        print("\n" * 100)

