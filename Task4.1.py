import random

def pick_word():
    return random.choice(word_bank)

def show_word(word, guessed_letters):
    revealed = ""
    for letter in word:
        if letter in guessed_letters:
            revealed += letter + " "
        else:
            revealed += "_ "
    return revealed[:-1]  

def display_hangman(tries):
    stages = [  
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
    return stages[tries]

def play_hangman():
    word = pick_word()
    guessed_letters = []
    tries = 0
    max_tries = len(display_hangman(0).split('\n')) - 1

    print("Welcome to the Hangman Game!")
    
    while tries < max_tries:
        print(display_hangman(tries))
        print(show_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            tries += 1

    else:
        print(display_hangman(tries))
        print("Sorry, you ran out of tries. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing!")

word_bank = ["python", "hangman", "programming", "computer", "algorithm", "openai", "language", "simulation", "intelligence", "artificial"]
play_hangman()
