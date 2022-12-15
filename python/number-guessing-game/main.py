import random
import time
import sys

#function to print a string with a delay
def print_with_delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

#function to print a string with a delay and a new line
def print_with_delay_new_line(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


# game intro
print_with_delay("Welcome to the number guessing game!")
print_with_delay("You have 5 chances to guess the number between 1 and 10")
print_with_delay("Let's begin!")

# generate a random number
random_number = random.randint(1, 10)

# set the number of guesses
number_of_guesses = 5

# set the number of guesses to 0
number_of_guesses_taken = 0

# set the game over flag to false
game_over = False

# while the game is not over
while not game_over:
    # get the user's guess
    guess = int(input("Guess a number between 1 and 10: "))

    # increment the number of guesses taken
    number_of_guesses_taken += 1

    # if the guess is correct
    if guess == random_number:

        print_with_delay_new_line("You guessed the number!")
        # set the game over flag to true
        game_over = True
    # if the guess is incorrect
    else:
        # if the number of guesses taken is less than the number of guesses
        if number_of_guesses_taken < number_of_guesses:
            # if the guess is too low
            if guess < random_number:
        
                print_with_delay_new_line("Your guess is too low!")
            # if the guess is too high
            else:
        
                print_with_delay_new_line("Your guess is too high!")
        # if the number of guesses taken is equal to the number of guesses
        else:
    
            print_with_delay_new_line("You ran out of guesses!")
            # set the game over flag to true
            game_over = True
print_with_delay_new_line("Thanks for playing!")

# print the number of guesses taken
print_with_delay_new_line("You took " + str(number_of_guesses_taken) + " guesses.")

# print the random number
print_with_delay_new_line("The number was " + str(random_number) + ".")
print_with_delay_new_line("Goodbye!")





