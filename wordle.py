import random

def load_words():
    return ["apple", "grape", "peach", "berry", "melon"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def get_guess():
    guess = input("Enter your guess (a single letter): ").lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Invalid input. Please enter a single letter: ").lower()
    return guess

def play_game():
    word_list = load_words()
    word = choose_word(word_list)
    guesses = []
    attempts = 6

    print("Welcome to Wordle!")
    print(display_word(word, guesses))

    while attempts > 0 and set(word) - set(guesses):
        guess = get_guess()
        if guess in guesses:
            print(f"You already guessed '{guess}'")
        elif guess in word:
            guesses.append(guess)
            print(f"Good guess! {display_word(word, guesses)}")
        else:
            attempts -= 1
            guesses.append(guess)
            print(f"Wrong guess. Attempts left: {attempts}")
            print(display_word(word, guesses))

    if set(word) - set(guesses):
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")
    else:
        print("Congratulations! You've guessed the word!")

if __name__ == "__main__":
    play_game()
