#HANGMAN 

import random 

words = ["python","hangman","programming","computer","alogrithm","openai","language","simulation","intelligence","artificial"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.rstrip()

def show_hangman(tries):
    drawing = [
        """
           --------
           |      |
           |      
           |      
           |      
           |     
        """,
        """
           --------
           |      |
           |      O
           |     
           |     
           |    
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           |    
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |     
           |    
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     
           |    
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |    
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |    
        """
    ]
    return drawing[tries]

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 0
    max_tries = len(show_hangman(0).split('\n')) - 1

    print("Welcome to Hangman Game!")

    while tries < max_tries:
        print(show_hangman(tries))
        print(display_word(word, guessed_letters))


        guess = input("Guess a letter:  ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter. ")
            continue

        if guess in guessed_letters:
           print("You've already guessed that letter.")
           continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word: :) ", word)
                return
        else:
            print("Incorrect Guess :( ")
            tries += 1

    else:
        print(show_hangman(tries))
        print("You Ran out of tries. The word was: ", word)
        

    play_again = input("Do you want to play the game again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing! ")


play_hangman()