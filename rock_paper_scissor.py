import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    print("__ " * 12)

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    print("__ " * 12)

    if user_input == "rock" and computer_pick == "scissors":
        print("You WON!")
        print("__ " * 12)

        user_wins += 1


    elif user_input == "paper" and computer_pick == "rock":
        print("You WON!")
        print("__ " * 12)

        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You WON!")
        print("__ " * 12)

        user_wins += 1

    else:
        print("You LOST!")
        computer_wins += 1

print("You WON", user_wins, "times.")
print("__ "*12)

print("The computer WON", computer_wins, "times.")
print("__ "*12)

print("Goodbye!!!!!")
print("__ "*12)

