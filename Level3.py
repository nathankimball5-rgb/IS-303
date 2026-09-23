
number_of_guesses = 1

decision = "y"

while(decision == "y" or decision == "Y"):

    import random
    number = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        print("I'm thinking of a number between 1 and 100.")
        input_number = int(input("Enter your guess: "))
        number_of_guesses += 1

        if(input_number >= 0 and input_number <= 100):

            if(input_number < number):
                print("Your guess is too low. Try again.")
                print("You have made " + str(number_of_guesses) + " guesses.")
            elif(input_number > number):
                print("Your guess is too high. Try again.")
                print("You have made " + str(number_of_guesses) + " guesses.")
            elif(input_number == number):
                print("It took you " + str(number_of_guesses) + " guesses.")
                if(number_of_guesses <= 3):
                    print("Amazing!")
                elif(number_of_guesses <= 5):
                    print("Impressive!")
                elif(number_of_guesses <= 7):
                    print("Good job!")
                elif(number_of_guesses <= 9):
                    print("Took a little longer, but you got there!")
                else:
                    print("You need to lock in.")
                break
        else:
            print("Please enter a number between 1 and 100.")
            input_number = int(input("Enter your guess: "))

    decision = input("Would you like to play again? (y/n): ")


