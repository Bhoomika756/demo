import random

def hangman():
    word_list = ["python", "hangman", "program", "developer", "coding"]
    chosen_word = random.choice(word_list)
    word_display = ["_"] * len(chosen_word)
    guessed_letters = []
    attempts_left = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word letter by letter.")

    while attempts_left > 0 and "_" in word_display:
        print("\nWord: " + " ".join(word_display))
        print(f"Attempts left: {attempts_left}")
        print("Guessed letters:", " ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess
            print("✅ Good guess!")
        else:
            attempts_left -= 1
            print("❌ Wrong guess.")

    if "_" not in word_display:
        print("\n🎉 You won! The word was:", chosen_word)
    else:
        print("\n💀 Game over! The word was:", chosen_word)

hangman()
