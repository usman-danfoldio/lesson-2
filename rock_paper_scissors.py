import random
Rock="#"
Paper="$"
Scissors="%"
game=[Rock, Paper, Scissors]
User_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if User_choice >= 3 or User_choice < 0 :
    print("You typed an invalid number, you lose!")
else:
    print(game[User_choice])

    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(game[computer_choice])
    

    if User_choice== 0 and computer_choice==2:
        print("You win")
    elif computer_choice==0 and User_choice==2:
        print("You lose") 
    elif computer_choice> User_choice:
        print("You lose")
    elif User_choice> computer_choice:
        print("You win")
    elif computer_choice== User_choice:
        print("it is a draw")
