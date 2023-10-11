# To install modules use (pip install <Module Name>) in terminal
# Use the datetime module when working with Time
# After installing datetime, it need to be imported into your program
# Importing allows access to the functions the datetime module contains.
import datetime

# Declare Global Variables and initialize by setting default values
# These variables store all of the necessary information
# for the algorithm to work.
main_loops = 2
main_loop_counter = 0
current_year = 0
age = 0
birth_year = 0

# It is a good idea to build in a method to control while loops
# The variable loop_counter is used.
while loop_counter < main_loops:
    # Get Imput from the user, inform them about value inputs
    age_input = input("Please enter your age (numbers only): ")
    
    # The algorithm should not execute with invalid input
    # If age_input is a digit (True) then continue
    # This is called input validation
    if age_input.isdigit():
        # Once the input has been validated, cast the input variable into an integer
        age = int(age_input)
        # Get the current year
        current_year = datetime.datetime.now().year
        # Calculate the birth year
        birth_year = current_year - age
        # Output Year of Birth 
        print("You were born in the year", birth_year,".")
        # Using Python Format (advanced)
        #print(f"You were born in the year {birth_year}.")
        
        # At the end of each loop change the counter
        loop_counter = loop_counter + 1
    else:
        # Inform the user of the else condition
        print("Invalid input. Please enter your age using numbers only.")
        break
else:
    # Inform the user of the else condition
    print("You only have", main_loops, "attempts")
    
