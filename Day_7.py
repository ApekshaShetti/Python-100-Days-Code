import random

print(
    """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      """
)
stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
word_list = ["apeksha", "neha", "vinay", "zaid"]
choosen_word = random.choice(word_list)

lives = 0
display = []
word_length = len(choosen_word)

for i in choosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Already entered this letter and correct one")
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in choosen_word:
        print("You guessed the wrong letter")
        lives += 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
