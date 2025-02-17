import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option_list = [rock, paper, scissors]
# input
your_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while your_selection > 2 or your_selection < 0:
    your_selection = int(input("Invalid input. Do it again.\n"))

pc_selection = random.randint(0, 2)
print(option_list[your_selection])
print("Computer chose:\n", option_list[pc_selection])

if your_selection == pc_selection:
    print("Tie.")
elif (your_selection == 0 and pc_selection == 1) or (your_selection == 1 and pc_selection == 2) or (your_selection == 2 and pc_selection == 0):
    print("You lose")
else:
    print("You win")
