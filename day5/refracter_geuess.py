# Secret Number Guessing Game


def get_guess():
    """Ask the user for a guess and return it."""
    guess = int(input("Guess the number: "))
    return guess


def is_guess_correct(guess, secret_number):
    """Return True if the guess is correct."""
    return guess == secret_number


def show_hint(difference):
    """Display a hint based on the difference."""

    if difference >= 4:
        print("Too Low!")

    elif 2 <= difference <= 3:
        print("Low")

    elif difference == 1 or difference == -1:
        print("Very Close")

    elif -3 <= difference <= -2:
        print("High")

    else:
        print("Too High!")


def guess_game():
    """Control the complete game."""

    secret_number = 7

    while True:

        guess = get_guess()

        if is_guess_correct(guess, secret_number):
            print("🎉 Congratulations! You guessed correctly.")
            break

        difference = secret_number - guess

        show_hint(difference)


# Start the game
guess_game()