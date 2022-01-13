import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulties = input("Choose a difficulty. Type 'easy' or 'hard' : ")
computer_guesses = random.randint(1, 100)


def compare ():
    if my_guess == computer_guesses:
        print("You guess the number. You win!")
    elif my_guess > computer_guesses:
        print("you chose, It's too high")
    else:
        print("you chose, It's too low")



def play ():
    missions = 0
    be_continue = True
    if difficulties == "easy":
        missions = 10
        while be_continue:
            print(f"You have {missions} attempts remaining to guess the number.")
            global my_guess
            my_guess= int(input("Make a Guess : "))
            compare()
            missions -= 1
            if missions == 0:
                print("You losing the game")
                be_continue = False
    if difficulties == "hard":
        missions = 5
        while be_continue:
            print(f"You have {missions} attempts remaining to guess the number.")
            my_guess = int(input("Make a Guess : "))
            compare()
            missions -= 1
            if missions == 0:
                print("you losing the game")  
                be_continue = False  
            
            
    

play()
again = input("Do you want play again? type 'y' to play again and type 'n' to close the game: ")    
if again == "y":
    play()
else:
    print("good for you, Bye!")
    exit()
        



