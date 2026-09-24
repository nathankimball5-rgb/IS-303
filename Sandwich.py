user_choice = "Y"
import random
#while user has pressed" "y"
while user_choice == "Y" or user_choice == "y":

    #computer generates a random number between 1 and 100.
    number = random.randint(1, 100) 
    num_guesses = 0
    guess = 0
    # while the user has not guessed the number
    
    while guess != number:

        #Ask the user for a guess between 1 and 100. 
        print("I'm thinking of a number between 1 and 100.")
        guess = int(input("Enter your guess: "))

        #While the guess is < 1 or > 100 
        while guess < 1 or guess > 100:
            print ("Invalid guess, please try again")
            guess = int(input("Enter your guess: "))

        num_guesses += 1

        if guess > number:
            print("Guess lower")

        elif guess < number:
            print("Guess higher")

        #Loop ends

    #Print the number of guesses 
    print("Correct!")
    print("You got it in " + str(num_guesses) + " guesses!")

    if num_guesses <= 3:
        print("Amazing!")
    elif num_guesses <=5:
        print("Impressive!")
    elif num_guesses <=7:
        print("Good job!")
    elif num_guesses <=9:
        print("Took a little longer, but you got there!")
    elif num_guesses >= 10:
        print("You need to lock in.")

    #Ask user to press "y" if they want to play again. 
    user_choice=input("If you'd like to play again press y if not press any other key:")

#loop