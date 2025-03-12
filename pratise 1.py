import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:  # Outer loop to allow multiple games
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10

        print(f"\nYou have {max_attempts} attempts to guess the number.")

        while attempts < max_attempts:  # Inner loop for guessing
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue  # Skip to the next iteration

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the inner loop when the guess is correct

        else:  # Executes if the loop finishes without a break
            print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # Exit the outer loop if the user doesn't want to play again

# Run the game
number_guessing_game()