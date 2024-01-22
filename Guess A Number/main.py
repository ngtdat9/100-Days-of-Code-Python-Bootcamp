import random
from art import logo

hard_mode = 5
easy_mode = 10

def check_answer(guess,number,turn):
    if guess > number:
        print("Too high")
        return turn - 1
        
    elif guess < number:
        print("Too low")
        return turn - 1
    else:
        print(f"Correct!! The number is {guess}.")
    
def set_difficulty():
    level = input("Type 'easy' or 'hard': ")
    if level == 'easy':
        return easy_mode
    elif level == 'hard':
        return hard_mode

def play_game():
    print("Welcome to the number guessing game!!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    number = random.randint(1, 101)
    guess = 0
    while guess != number:
        guess = int(input(f"You have {turns} attempts. Try to guess a number: "))
        turns  = check_answer(guess, number, turns)
        if turns == 0:
            print("Out of turns. You lose!!")
            return
        elif guess != number:
            print("guess again")

        

print(logo)
play_game()



