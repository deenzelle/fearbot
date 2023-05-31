# COMPONENT 2
# VERSION 4

# Asks the user how they would prefer to have their order handled
print("Do you want your order delivered or are you planning to click & collect?")
print("To select delivery enter '1'")
print("To select Click & Collect enter '2'")

while True:
    try:
        # Sets the delivery variable to the integer inputted (ideally it should be either 1 or 2)
        delivery = int(input())
        if delivery >= 1 and delivery <= 2: # Checks to see if the number is greater than or equal to 1, or less than or equal to 2
            if delivery == 1: # Checks to see if the input entered is '1', if so, the program will print 'Delivery' then break out of loop
                print ("Delivery")
                break
            
            elif delivery == 2:  # Checks to see if the input entered is '2', if so, the program will print 'Click and Collect' then break out of loop
                print("click and collect") # Clearly states what the user has to enter to proceed with their order
                break
                
        else: # If the input was not one of those two, the program will print this message
            print("Please pick between 1 (Delivery) or 2 (Click and Collect)")

    except ValueError: # Only happens if the user has entered a letter for an input
        print("That is not a valid number") # Only allows numbers to be a valid input
        print("Please pick between 1 (Delivery) or 2 (Click and Collect)") # Clearly states what the user has to enter to proceed with their order
