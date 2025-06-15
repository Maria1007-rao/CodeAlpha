import random
word_list = ["apple", "chair", "snake", "house", "bread"]
selected_word = random.choice(word_list)
word_length = len(selected_word)
guessed_word = ["_"] * word_length
max_attempts = 6
wrong_attempts = 0
guessed_letters = []

print("Welcome to the Hangman Game!")
print("Guess the word, one letter at a time.")
while "_" in guessed_word and wrong_attempts < max_attempts:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in selected_word:
        print("Correct guess!")
        for i in range(word_length):
            if selected_word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_attempts += 1
        print(f"Wrong guess! Remaining attempts: {max_attempts - wrong_attempts}")
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", selected_word)
else:
    print("\n Game Over! The correct word was:", selected_word)
