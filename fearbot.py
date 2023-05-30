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
    
main() # Runs the main function