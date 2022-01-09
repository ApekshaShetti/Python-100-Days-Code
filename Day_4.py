import random

list = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

choice = int(
    input('What do you choose? Type "0" for Rock,"1" for Paper or "2" for Scissors.\n')
)
print("You chose", list[choice])
computerchoice = random.randint(0, 2)
print(f"Computer chose {computerchoice}")
print("Computer chose", list[computerchoice])
if choice == 0 and computerchoice == 1:
    print("Computer wins")
elif choice == 0 and computerchoice == 0:
    print("draw")
elif choice == 0 and computerchoice == 2:
    print("You win")
elif choice == 1 and computerchoice == 0:
    print("You win")
elif choice == 1 and computerchoice == 1:
    print("draw")
elif choice == 1 and computerchoice == 2:
    print("Computer wins")
elif choice == 2 and computerchoice == 2:
    print("draw")
elif choice == 2 and computerchoice == 0:
    print("Computer Wins")
elif choice == 2 and computerchoice == 1:
    print("You win")
