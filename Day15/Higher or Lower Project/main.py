import game_data
import random
import art

def display_data(option):
    name = option["name"]
    description = option["description"]
    country = option["country"]
    return f"{name}, a {description}, from {country}"

def compare_data(option1, option2):
    follower_count_a = int(option1["follower_count"])
    follower_count_b = int(option2["follower_count"])
    if follower_count_a > follower_count_b:
        return "A"
    else:
        return "B"

print(art.logo)
should_continue = True
score = 0
option_B = random.choice(game_data.data)

while should_continue:
    option_A = option_B
    option_B = random.choice(game_data.data)

    if option_A == option_B:
        option_B = random.choice(game_data.data)

    print(f"Compare A: {display_data(option_A)}")
    print(art.vs)
    print(f"Against B: {display_data(option_B)}")

    player = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    print("\n" * 25)
    print(art.logo)
    if player == compare_data(option_A, option_B):
        score += 1
        print(f"You're right! current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        should_continue = False
