from random import randint


print("I Picked a number between 1-100, Take a guess!");
num1 = randint(1,100);


def getUserGuess():
    while True:
        try:
            userguess = int(input("What is your guess? \n"));
            return userguess
        except ValueError:
            print("That is not a number.");
    

attempts = 0

while True:
    userguess = getUserGuess();
    attempts += 1

    if userguess < 1 or userguess > 100:
        print(("Your guess is out of bounds. Pick a number between 1-100. \n"));
        
    
    elif userguess < num1:
        print("My number is bigger than your guess.");
    
    elif userguess > num1:
        print("My number is smaller than your guess");

    else:
        break;


print(f"Congratulations! Number I picked was: {num1}. It took you {attempts} attempts. ");