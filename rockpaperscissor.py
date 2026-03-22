import random 


print(
        "Winning rules of the game ROCK PAPER SCISSORS are:\n"
        "Rock vs Paper -> Paper wins \n"
        "Rock vs Scissors -> Rock wins \n"
        "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter the choice of the Rock -1; Scissor-2; Paper-3")

    choice = int(input("Enter the choice number or the required number to be passed "))
                 
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else :
        comp_choice_name = 'Scissor'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")