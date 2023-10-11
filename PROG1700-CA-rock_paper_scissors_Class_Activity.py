# Comments

# Import modules here
import random

# Global Variables
# Program Attempts, Change the variable to the number of rounds.
invalid_attempts = 3
# Variable to control the random computer player value
start = 0
stop = 3
step = 1

# Program Control
while invalid_attempts > 0:
    # Local Variable user_input
    user_input = input("Press 1 for rock, 2 for paper, 3 for scissors:")
    # Validate the input to ensure the program does not have invalid input
    # Return true is a digit is entered, otherwise return false
    if user_input.isdigit():
        # Only accept 1 digit
        if len(user_input) == 1:
            # Cast to an integer
            user_input = int(user_input)
            # 1,2,3 numbers only
            # Calculate the computer's value
            computer_value = random.randrange(start,stop, step)
            # computer_value = random.randint(1,3)
            # print computer value for troubleshooting or verify the o/p of random function
            #print(computer_value)
            
            if user_input != computer_value:
                # Check when user_input is 1
                # User Wins when
                # user_input = 1 and computer_value = 3 or computer value = 2
                # Else computer wins
                if user_input == 1 and computer_value == 3 or user_input == 2 and computer_value == 1 or user_input == 3 and computer_value == 2:
                    print("User Wins")
                else:
                    print("Computer Wins")
            else:
                print("Tie Game")
        else:
            print("Please enter a single digit")
            invalid_attempts = invalid_attempts - 1
            print("You have", invalid_attempts,"attempts")
    else:
        print("Invalid Input")
        invalid_attempts = invalid_attempts - 1
        print("You have", invalid_attempts,"attempts")
else:
    print("You have no intentions of playing fairly.  Bye")