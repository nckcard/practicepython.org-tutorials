import random


def compare_numbers(num1,num2):
    cows = 0
    bulls = 0

    for i in range(len(num1)):
        if num1[i] in num2:
            if num1[i] == num2[i]:
                cows += 1
            else:
                bulls += 1
                
    return cows, bulls
            


if __name__=="__main__":
    playing = True
    sol = random.randrange(0,9999)
    guesses = 0
    print(sol)

    while playing:
        user_guess = input("Guess a 4 digit number: ")
        if user_guess == "exit":
            break

        cowsbulls = compare_numbers(str(sol),user_guess)
        guesses += 1

        print("You have " + str(cowsbulls[0]) + " cows and " + str(cowsbulls[1]) + " bulls.")
        
        if cowsbulls[0] == 4:
            playing = False
            print("You won in " + str(guesses) + " guesses!")
