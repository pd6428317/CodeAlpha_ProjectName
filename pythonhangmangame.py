import random

words = ["apple", "chair", "table", "plant", "house"]
word_to_guess = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses allowed.\n")

while wrong_guesses < max_wrong:
    # Show current state of word
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Word:", " ".join(display_word))
    print(f"Incorrect guesses left: {max_wrong - wrong_guesses}")
# Check if player has won
    if "_" not in display_word:
        print("\n🎉 You guessed the word correctly:", word_to_guess)
        score = max_wrong - wrong_guesses  # calculate score
        print(f"Your score: {score}/{max_wrong}")
        break

    # Get user input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter a single letter (a-z).")
        continue
    if guess in guessed_letters:
        print("❌ You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print(f"✔ Good job! '{guess}' is in the word.")
    else:
        wrong_guesses += 1
        print(f"✖ Sorry! '{guess}' is NOT in the word. Mistakes: {wrong_guesses}/{max_wrong}")

# If loop ends without winning → player loses
if "_" in display_word:
    print("\n💀 Game Over! You've used all your incorrect guesses.")
    print("The word was:", word_to_guess)
    score = max_wrong - wrong_guesses  # calculate score (will be 0)
    print(f"Your score: {score}/{max_wrong}")