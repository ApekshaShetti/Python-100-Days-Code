# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a level. Type 'Easy' or 'Hard': ").lower()
actual_number = random.randint(1, 100)
if level == "easy":
    should_continue = 10
else:
    should_continue = 5
while should_continue > 0:
    print(f"You are left with {should_continue} chances")
    should_continue = should_continue - 1
    guess = int(input("Make a guess: "))
    if guess > actual_number:
        print("You are too high")
    elif guess < actual_number:
        print("You are two low")
    else:
        print("Yayyy! You are right...")
        break
