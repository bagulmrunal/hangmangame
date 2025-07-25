#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def hangman():
    # Predefined list of 5 words
    words = ['apple', 'table', 'chair', 'grass', 'mouse']
    
    # Choose one word randomly
    word = random.choice(words)
    
    # Track guessed letters and number of wrong guesses
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    # Create a display version of the word (e.g., "_ _ _ _ _")
    display_word = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", max_wrong, "incorrect guesses.\n")

    # Game loop
    while wrong_guesses < max_wrong and '_' in display_word:
        print("Word:", ' '.join(display_word))
        guess = input("Enter a letter: ").lower()

        # Check input validity
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
            # Reveal all matching letters in the display
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong guess!\n")
            wrong_guesses += 1
            print("Incorrect guesses:", wrong_guesses, "/", max_wrong)

    # Final outcome
    if '_' not in display_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

# Run the game
hangman()


# In[ ]:




