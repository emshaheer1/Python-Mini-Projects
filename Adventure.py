name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
print("__ "*12)

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
print("__ "*12)

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    print("__ " * 12)

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
        print("__ " * 12)
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
        print("__ " * 12)

    else:
        print('Not a valid option. You lose.')
        print("__ " * 12)

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    print("__ " * 12)

    if answer == "back":
        print("You go back and lose.")
        print("__ " * 12)
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        print("__ " * 12)

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
            print("__ " * 12)
        elif answer == "no":
            print("You ignore the stranger and they are offended and You LOSE!.")
            print("__ " * 12)
        else:
            print('Not a valid option. You LOSE!.')
            print("__ " * 12)
    else:
        print('Not a valid option. You LOSE!.')
        print("__ " * 12)

else:
    print('Not a valid option. You LOSE!.')
    print("__ " * 12)

print("Thank you for trying", name)
print("__ "*12)