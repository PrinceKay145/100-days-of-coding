#Step 5

import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for p in range(word_length):
      letter = chosen_word[p]
      if guess in display:
        print(f"You already guessed {guess}, that's a repetition")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #used to keep a track of what you've guessed and where it was placed
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word to guess, You loose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"the correct answer is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
