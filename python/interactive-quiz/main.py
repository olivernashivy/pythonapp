# build an interactive quiz

# import the random module
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
print_with_delay("Welcome to the interactive quiz!")
print_with_delay("You will be asked 5 questions.")
print_with_delay("Let's begin!")

# set the number of questions
number_of_questions = 5

# set the number of questions to 0
number_of_questions_taken = 0

# set the game over flag to false
game_over = False

question_list =[ {
    "id":1,
    "question": "What is the capital of France?",
    "answer": "Paris"
    },
    {
    "id":2,
    
    }

    
    
    ]


# while the game is not over

while not game_over:
    # get the user's guess
    question = random.choice(question_list)
    answer = input(question)
    question_list.remove(question)
    # increment the number of questions taken
    number_of_questions_taken += 1

    # if the guess is correct
    if answer == answer_list[number_of_questions_taken - 1]:

        print_with_delay_new_line("You guessed the answer!")
        # set the game over flag to true
        game_over = True
    # if the guess is incorrect
    else:
        # if the number of questions taken is less than the number of questions
        if number_of_questions_taken < number_of_questions:
            # if the guess is too low
            if answer < answer_list[number_of_questions_taken - 1]:

                print_with_delay_new_line("Your guess is too low!")
            # if the guess is too high
            else:

                print_with_delay_new_line("Your guess is too high!")
        # if the number of questions taken is equal to the number of questions
        else:
            # set the game over flag to true
            game_over = True
            # print the correct answer
            print_with_delay_new_line("The correct answer is " + answer_list[number_of_questions_taken - 1] + ".")
            # print the game over message
            print_with_delay_new_line("Game over!")
    
