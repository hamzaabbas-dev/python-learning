import random


def guess_number():
    """Run a number guessing game with input validation."""

    # Choose the secret number once for the entire game.
    secret_number = random.randint(1, 99)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 99.")

    while True:
        # Handle text, empty input, and other non-integer values.
        try:
            user_number = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        # Reject numbers outside the allowed range.
        if not 1 <= user_number <= 99:
            print("Please enter a number between 1 and 99.")
            continue

        # Only valid guesses count as attempts.
        attempts += 1

        # End the game when the player finds the secret number.
        if user_number == secret_number:
            print(f"Congratulations! You won in {attempts} attempts.")
            break

        # Give a hint to help the player make the next guess.
        elif user_number < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print("Thanks for playing!")


# Start the game only when this file is run directly.
if __name__ == "__main__":
    guess_number()