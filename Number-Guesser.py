import random

top_of_range = input("Type a number: ")
print("__ " * 12)


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        print("__ " * 12)
        quit()
else:
    print('Please type a number next time.')
    print("__ " * 12)
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    print("__ " * 12)
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        print("__ " * 12)
        continue

    if user_guess == random_number:
        print("You got it!")
        print("__ " * 12)
        break
    elif user_guess > random_number:
        print("You were above the number!")
        print("__ " * 12)
    else:
        print("You were below the number!")
        print("__ " * 12)

print("You got it in", guesses, "guesses")

print("__ " * 12)