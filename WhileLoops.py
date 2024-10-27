### Part Two -- your code goes here. 
import random
number =random.randint(1, 100)

guessNum = None

while guessNum != number:
    guessNum = int(input("Guess a number between 1 and 100: ")) 
    
    if guessNum < number:
        print("Your number is too low! Please try again.")
    elif guessNum > number:
        print("Your number is too high! Please try again.")
    else:
        print("Well done!!, you have guessed the right number.")