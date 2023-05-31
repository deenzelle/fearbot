# COMPONENT 2
# VERSION 3

# Asks the user how they would prefer to have their order handled
print("Do you want your order delivered or are you planning to click & collect?")
print("To select delivery enter '1'")
print("To select Click & Collect enter '2'")

# Sets the delivery variable to the integer inputted (ideally it should be either 1 or 2)
delivery = int(input())

# Note: Once an invalid integer input has been entered, the program does not loop back to ask the user again
if delivery == 1: # Checks to see if the input entered is 'd', if so, the program will print 'Delivery' then end
    print ("Delivery")
elif delivery == 2:  # Checks to see if the input entered is 'c', if so, the program will print 'Click and Collect' then end
    print("click and collect")
else: # If the input was not one of those two, the program will print this message
    print("That was not a valid input")
