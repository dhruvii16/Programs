import random

user_choice=int(input("Enter your choice: Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS."))
if user_choice>=3 or user_choice<0:
    print("You Entered invalid number, You Loose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice==user_choice:
        print("It is draw.")
    elif computer_choice==0 and user_choice==2:
        print("You Loose.")
    elif user_choice==0 and computer_choice==2:
        print("You Win.")
    elif computer_choice > user_choice:
            print("You Loose.")
    elif user_choice > computer_choice:
            print("You Win.")