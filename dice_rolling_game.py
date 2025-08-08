import random

roll_count = 0 # New variable to track rolls

while True:
    choice = input("Roll the dice (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
        roll_count += 1 # Increment the counter
    elif choice == "n":
        print(f"You rolled the dice {roll_count} times. Thanks for playing!")
        break
    else:
        print("You have entered an invalid input")
