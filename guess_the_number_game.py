import random
def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 6
    while attempts > 0:
        print("You have", attempts, "guesses remaining.")
        try:
            guess = int(input("What's your guess? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess < 1 or guess > 20:
            print("Please choose a number between 1 and 20.")
            continue
        if guess == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        attempts -= 1
    if attempts == 0:
        print("Sorry, you're out of guesses. The number was:", secret_number)
if __name__ == "__main__":
    guess_the_number()

