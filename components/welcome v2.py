# COMPONENT 1
# VERSION 2

# Imports a library that allows the program to have randomness where nescessary
import random
from random import randint # Imports the ability to choose between integers randomly

# List of names
names = ["Hanni", "Chaewon", "Nicole", "Kaitlin", "Denzelle", "Harry", "Yeonjun", "Jaehyun", "Jungkook", "Sunghoon"]

# Defines a welcome function to contains the banner/welcome message
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
    
# Calls the function/Tells the program to run a specific function
def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()
    
main()