import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

def choose_word(word_list):
    # Randomly select a word from the list
    return random.choice(word_list)

def play_hangman():
    word = choose_word(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman! Guess the fruit")
    
    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print("Incorrect guess.")
        else:
            print("Invalid input. Please enter a single letter.")
        
        if set(guessed_letters) == set(word):
            print("Congratulations! You've guessed the word:", word)
            break
    
    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()
