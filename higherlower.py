# guessing a number between 1-100, easy --> 10 guesses, hard ----> 5 guesses.
import random


#Global variables
guesses = 0


#random number
random_num = random.randint(0,100)

#functions
def user_choice(guess):
    return f"You have {guess} attempts remaining to guess the number."



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user_difficulty.lower() == 'easy':
    guesses = 10
elif user_difficulty.lower() == 'hard':
    guesses = 5

user_choice(user_difficulty) ## Sets guesses to a number but doesn't print


for i in range(guesses):
    print(user_choice(guesses))  # Used user-choice function to print the amount of guesses
    user_guess = int(input("Make a Guess: "))
    if user_guess > random_num:
        print("Too High")

    elif user_guess < random_num:
        print("Too Low")

    guesses = guesses - 1
    if guesses == 0:
        print('You have ran out of guesses. You lose!')
    else:
        print("Guess again")






