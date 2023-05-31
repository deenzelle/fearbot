# FEARBOT Program
# A progam that can be used by 'FEARNOT' to order LE SSERAFIM merch

# Imports a library that allows the program to have randomness where nescessary
import random
from random import randint # Imports the ability to choose between integers randomly

# List of names
names = ["Hanni", "Chaewon", "Nicole", "Kaitlin", "Denzelle", "Harry", "Yeonjun", "Jaehyun", "Jungkook", "Sunghoon"]

# Create a welcome function that welcomes the customer to the bot
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None 
    '''
    # Chooses a random integer between 0 and 9
    num = randint(0,9)
    # Sets the name variable equal to the name which corresponds to the above selected integer
    name = (names[num])
    # Prints out a welcome banner
    print("""
         _____ _____    _    ____  _   _  ___ _____    ____ _____ _   _ _____ ____      _    _     
        |  ___| ____|  / \  |  _ \| \ | |/ _ \_   _|  / ___| ____| \ | |_   _|  _ \    / \  | |    
        | |_  |  _|   / _ \ | |_) |  \| | | | || |   | |   |  _| |  \| | | | | |_) |  / _ \ | |    
        |  _| | |___ / ___ \|  _ <| |\  | |_| || |   | |___| |___| |\  | | | |  _ <  / ___ \| |___ 
        |_|   |_____/_/   \_\_| \_\_| \_|\___/ |_|    \____|_____|_| \_| |_| |_| \_\/_/   \_\_____|
        """)
    # Prints out basic welcome message
    print("*** Welcome to FEARNOT Central")
    print("*** My name is" ,name) # Prints out the randomly selected name
    print("*** I will be to help you order OFFICIAL LE SSERAFIM MERCHANDISE")

# Asks the user if the order is intended for click and collect or delivery
def order_type(): # Defines a new function for the order type
    '''
    Purpose: To ask the user how they want their order to be prepared, Click & Collect or Delivery
    Parameters: None
    Returns: None
    '''
    # Asks the user how they would prefer to have their order handled
    print("Do you want your order delivered or are you planning to click & collect?")
    print("To select delivery enter '1'") # Clearly states what the user has to enter to proceed with their order
    print("To select Click & Collect enter '2'") # Clearly states what the user has to enter to proceed with their order
    while True: # Creates a loop where while it is 'True', the program will continually ask the user to input either 1 or 2
        try:
            # Sets the delivery variable to the integer inputted (ideally it should be either 1 or 2)
            delivery = int(input())
            if delivery >= 1 and delivery <= 2: # Checks to see if the number is greater than or equal to 1, or less than or equal to 2
                if delivery == 1: # Checks to see if the input entered is '1', if so, the program will print 'Delivery' then break out of loop
                    print ("Delivery")
                    break
                
                elif delivery == 2:  # Checks to see if the input entered is '2', if so, the program will print 'Click and Collect' then break out of loop
                    print("click and collect")
                    break
                    
            else: # If the input was not one of those two, the program will print this message
                print("Please pick between 1 (Delivery) or 2 (Click and Collect)") # Clearly states what the user has to enter to proceed with their order

        except ValueError: # Only happens if the user has entered a letter for an input
            print("That is not a valid number") # Only allows numbers to be a valid input
            print("Please pick between 1 (Delivery) or 2 (Click and Collect)") # Clearly states what the user has to enter to proceed with their order

# Collects the user's name, address and phone number if order is intended for delivery

# Collects the user's name and phone number as well as notifying the user that they will receive a text message if order was intended for click and collect

# Make a menu of at least 12 items for the user to choose from
# Make each item available item orderable
# Make the cost of each item display within the menu

# Prints out order details
# Items & Prices
# Total cost of order, incl delivery charge (if applicable)
# Customer's name
# Customer's phone number
# (IF ORDER IS FOR DELIVERY) Print out customer's address

# Asks the user if they wish to cancel the order before submitting it

# Ask if user wishes to place another order, or exit the bot

# Calls the function/Tells the program to run a specific function
def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()
    order_type()
    
main() # Runs the main function