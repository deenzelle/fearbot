# COMPONENT 2
# VERSION 2

# Asks the user how they would prefer to have their order handled
print("Do you want your order delivered or are you planning to click & collect?")
print("To select delivery enter 'd'")
print("To select Click & Collect enter 'c'")

# Sets the delivery variable to what has been inputted
delivery = input()

# Note: Once an invalid input has been entered, the program does not loop back to ask the user again
# Note: The program is strict on only allowing 'd' and 'c', and not 'D' and 'C'
if delivery == "d": # Checks to see if the input entered is 'd', if so, the program will print 'Delivery' then end
    print ("Delivery")
elif delivery == "c":  # Checks to see if the input entered is 'c', if so, the program will print 'Click and Collect' then end
    print("click and collect")

else: # If the input was not one of those two, the program will print this message
    print("That was not a valid input")
