import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
# print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try something else.\n")
        continue 

    display = ""

    for letter in chosen_word:
        if letter == guess:
            print("You've chosen the correct letter!")
            correct_letters.append(guess)
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print("Word to guess: " + display)

        if lives == 0:
            print(stages[lives])
            print(f"*********************** IT WAS '{chosen_word.upper()}' — YOU LOSE **********************")
            game_over = True
        else:
            print(stages[lives])  

    else:
        print("Word to guess: " + display)
        print(stages[lives]) 

        if "_" not in display:
            print("**************************** YOU WIN ****************************")
            game_over = True