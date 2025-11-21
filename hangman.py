import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
    +---+
    |   |
    O   |
    |   |
   / \  |
        |
        |
=========''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', r'''
    +---+
    |   |
        |
        |
        |
        |
=========''']


word_list = ["mango","apple","banana","papaya","peach","grapes","orange","kiwi","watermelon","strawberry"]
chosen_word = random.choice(word_list)

# don't print the chosen word in a real game
# print(chosen_word)

lives = len(stages) - 1   # ensures stages[lives] is valid
guessed_letters = set()
game_over = False

# initial display of underscores
display = "_" * len(chosen_word)
print(display)

while not game_over:
    chosen_letter = input("Guess a letter: ").lower().strip()

    # input validation
    if not chosen_letter:
        print("Please type a letter.")
        continue
    if len(chosen_letter) != 1 or not chosen_letter.isalpha():
        print("Enter a single alphabetic character.")
        continue

    if chosen_letter in guessed_letters:
        print(f"You already guessed '{chosen_letter}'. Try a different letter.")
        print(stages[lives])
        continue

    # add to guessed set
    guessed_letters.add(chosen_letter)

    if chosen_letter in chosen_word:
        # rebuild display
        display = "".join([ch if ch in guessed_letters else "_" for ch in chosen_word])
        print(display)
    else:
        lives -= 1
        print(f"You guessed '{chosen_letter}', that's not in the word. You lose a life.")
        if lives < 0:
            # safety (shouldn't happen with correct lives/stages setup)
            lives = 0

    # show hangman stage
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print(f"You lose. The word was: {chosen_word}")
