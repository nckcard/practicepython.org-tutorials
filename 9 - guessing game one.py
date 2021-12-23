import random

secret_number = random.randrange(0,9)
chosen_number = -1
num_guesses = 1

while chosen_number != secret_number:
    chosen_number = int(input("Guess a number between 0-9: "))

    if chosen_number == secret_number:
        if num_guesses==1:
            print("You won in " + str(num_guesses) + " guess!")
        else:
            print("You won in " + str(num_guesses) + " guesses!")
    elif chosen_number > secret_number:
        print("Too high.")
        num_guesses+=1
    elif chosen_number < secret_number:
        print("Too low.")
        num_guesses+=1
        
