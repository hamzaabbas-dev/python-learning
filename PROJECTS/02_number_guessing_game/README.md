# Number Guessing Game 🐍

A command-line Python game where the player guesses a randomly selected number between 1 and 99.

I built this project to practise functions, loops, conditions, exception handling, and input validation as part of my Python learning journey.

## Features

- Random secret number for each game.
- Higher or lower hints after incorrect guesses.
- Attempt counter that counts only valid guesses.
- Input validation for letters, empty input, and decimal values.
- Range checking to accept only numbers from 1 to 99.
- A winning message showing the total attempts.

## Requirements

- Python 3
- A terminal

No external packages are required. The game uses Python's built-in `random` module.

## Project Files

| File | Purpose |
|------|---------|
| `main.py` | Game code |
| `README.md` | Project description and instructions |

## How to Run

1. Download or clone this repository.
2. Open a terminal inside `PROJECTS/02_number_guessing_game`.
3. Run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

4. Enter a number between 1 and 99.
5. Follow the hints until you find the secret number.

## Example Gameplay

This example assumes the secret number is 45. The actual number changes between games.

```text
Welcome to the Number Guessing Game!
I have chosen a number between 1 and 99.

Enter your guess: abc
Please enter a whole number.

Enter your guess: 150
Please enter a number between 1 and 99.

Enter your guess: 20
Too low! Try a higher number.

Enter your guess: 60
Too high! Try a lower number.

Enter your guess: 45
Congratulations! You won in 3 attempts.
Thanks for playing!
```

Invalid inputs do not increase the attempt counter.

## Concepts Practised

- Importing and using the `random` module.
- Defining and calling functions.
- Repeating actions with a `while` loop.
- Comparing values with `if`, `elif`, and `else`.
- Converting user input with `int()`.
- Handling invalid input with `try` and `except ValueError`.
- Using `continue` and `break`.
- Formatting messages with f-strings.
- Using the `__main__` guard.

## Manual Checks

Use these checks to verify the game:

| Input or action | Expected behaviour |
|-----------------|--------------------|
| Enter `abc` | Show an error and ask again |
| Submit empty input | Show an error and ask again |
| Enter `3.5` | Request a whole number |
| Enter `0` or `100` | Request a number between 1 and 99 |
| Guess below the secret number | Show “Too low” |
| Guess above the secret number | Show “Too high” |
| Guess the correct number | Show attempts and end the game |

## Future Improvements

- Add an option to play again.
- Add difficulty levels.
- Save the best score to a file.

## Author

**Hamza Abbas**

[GitHub Profile](https://github.com/hamzaabbas-dev)