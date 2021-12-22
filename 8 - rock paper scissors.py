import random

cont = True
player_score = 0
comp_score = 0

while cont==True:

    valid_choice = False

    while valid_choice == False:
        choice = input("Rock, Paper, or Scissors? ")

        if choice=="Rock":
            choice_num = 1
            valid_choice = True
        elif choice=="Paper":
            choice_num = 2
            valid_choice = True
        elif choice=="Scissors":
            choice_num = 3
            valid_choice = True
        else:
            valid_choice = False


    comp_choice = random.randrange(1,3)
    

    if choice_num==comp_choice:
        print("Tie!")
    elif choice_num==1:
        if comp_choice==2:
            print("Computer chose paper. You lose.")
            comp_score+=1
        elif comp_choice==3:
            print("Computer chose scissors. You win!")
            player_score+=1
            
    elif choice_num==2:
        if comp_choice==1:
            print("Computer chose rock. You win!")
            player_score+=1
        elif comp_choice==3:
            print("Computer chose scissors. You lose")
            comp_score+=1
            
    elif choice_num==3:
        if comp_choice==1:
            print("Computer chose paper. You lose.")
            comp_score+=1
        elif comp_choice==2:
            print("Computer chose paper. You win!")
            player_score+=1

    print("Player score: " + str(player_score))
    print("Computer score: " + str(comp_score))


    cont_choice = input("Play again? (Y/N): ")

    if cont_choice=="N":
        break
