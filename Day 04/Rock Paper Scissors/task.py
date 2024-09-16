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

choices = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_choice = choices[player]
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)
else:
    print("Please choose only 0, 1 or 2")


computer = random.choice(choices)
print(computer)

if player_choice == computer:
    print("It's a tie!")
elif player_choice == rock and computer == scissors or \
        player_choice == paper and computer == rock or \
        player_choice == scissors and computer == paper:
    print("You win!")
else:
    print("You lose")

