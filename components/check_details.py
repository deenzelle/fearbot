def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    # Call the welcome function to welcome the customer
    welcome()
    # Call the order_type function to determine the delivery or click & collect preference
    del_click = order_type()
    # Call the check_information function to ask user if the details entered are correct before proceeding
    check_information(del_click)
    
# FEARBOT Program
# A progam that can be used by 'FEARNOT' to order LE SSERAFIM merch
# dealing with comments when the internal is finished

# Imports a library that alLOWs the program to have randomness where necessary
import random
from random import randint  # Imports the ability to choose between integers randomly

# Import the sys module for system-related operations and functionality
import sys

# Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

# Creates the customer detail dictionary to have memory of user input of details
customer_details = {}

# List to store ordered merchandise items
order_list = []
# List to store ordered merchandise prices
order_cost = []

# List of names
names = ["Kazuha", "Chaewon", "Nicole", "Kaitlin", "Denzelle",
         "Yunjin", "Eunchae", "Jaehyun", "Jungkook", "Sakura"]

# List of merchandise items available to purchase
merch_names = [
    'FEARLESS ALBUM (BLACK PETROL VER)',
    'FEARLESS ALBUM (MONOCHROME BOUQUET VER)',
    'FEARLESS ALBUM (BLUE CYPHER VER)',
    'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)',
    'ANTIFRAGILE ALBUM (IRIDESCENT OPAL VER)',
    'ANTIFRAGILE ALBUM (MIDNIGHT ONYX VER)',
    'UNFORGIVEN ALBUM (DEWY SAGE VER)',
    'UNFORGIVEN ALBUM (DUSTY AMBER VER)',
    'UNFORGIVEN ALBUM (BLOODY ROSE VER)',
    'LE SSERAFIM LIGHT STICK',
    'LE SSERAFIM FLOOR MAT',
    'LE SSERAFIM TUMBLER',
    'LE SSERAFIM HOODIE'
]

# List of available merchandise prices
merch_prices = [
    69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50,
    45.50, 25.50, 15.50, 45.50
]

# Defines a function called not_blank, validates inputs to check if they are blank


def not_blank(question):
    '''
    Purpose: Validates user input to ensure it is not blank. If the input is blank, it prompts the user to enter a non-blank value.
    Parameters: Question
    Returns: The validated non-blank value as a title-cased string. response.title()
    '''
    valid = False
    while not valid:  # If not valid
        response = input(question)  # Prompt the user to enter a response
        if response != "":  # Check if the response is not blank
            # Returning the response also breaks the loop
            return response.title()  # Return the response as a title-cased string
        else:
            # Print an error message if the input is blank
            print("The input you provide cannot be blank")


# checks string to only contain letters
def check_string(question):
    '''
    Purpose: Validates user input as a string containing only alphabetic characters.
    Parameters:
    - question: The prompt message asking the user to enter a string.
    Returns: The validated string as a title-cased version if it consists only of alphabetic characters. ( response.title() )
    '''
    while True:
        response = input(question)  # Asks the user to enter a string
        x = response.isalpha()  # Checks if the string consists only of alphabetic characters
        if x == False:
            # Prints an error message if the input contains non-alphabetic characters
            print("Input must only contain letters")
        else:
            # Returns the string as a title-cased version if it consists only of alphabetic characters
            return response.title()
            # print(response.title())
            break


# phone number validation string
def check_phone(question, PH_LOW, PH_HIGH):
    '''
    Purpose: Validates user input as a phone number within a specified range of digit counts.
    Parameters:
    - question: The prompt message asking the user to enter a phone number.
    - PH_LOW: The lower boundary of the desired range.
    - PH_HIGH: The upper boundary of the desired range.
    Returns: The validated phone number as a string if it consists of digits and its length is within the specified range. str(num)
    '''
    while True:
        try:
            # Asks the user to enter a phone number as an integer
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:  # Loops through the digits of the number to count them
                test_num = test_num // 10  # Removes the last digit from test_num
                count = count + 1  # Adds 1 to the count
            if count >= PH_LOW and count <= PH_HIGH:  # Checks if the count of digits is within the specified range
                return str(num)  # Returns the phone number as a string
            else:
                print("NZ phone numbers have between 7 and 10 digits")

        except ValueError:
            # Prints an error message if a non-integer value is entered
            print("Please only enter numbers!")


# Defines a function, which validates inputs to check if they are an integer


def val_int(LOW, high, question):
    '''
    Purpose: Validates user input as an integer within a specified range.
    Parameters:
    - LOW: The lower boundary of the desired range.
    - high: The upper boundary of the desired range.
    - question: The prompt message asking the user to enter a number.
    Returns: The validated integer input within the specified range. (num)
    '''
    while True:
        try:
            num = int(input(question))  # Prompt the user to enter a number
            if num >= LOW and num <= high:  # Check if the number is within the desired range
                return num  # Return the number as an integer
            else:
                # Display an error message if the number is not within the desired range
                print(f"Enter a number between {LOW} and {high}")
        except ValueError:
            # Display an error message if the input is not a valid integer
            print("That is not a valid number")
            # Prompt the user to enter a number again
            print(f"Enter a number between {LOW} and {high}")


# Defines a welcome function that welcomes the customer to the bot
def welcome():
    '''
    Purpose: Generates a random name from a list and prints a welcome message.
    a welcome message
    Parameters: None
    Returns: None 
    '''
    # Chooses a random integer between 0 and 9
    num = randint(0, 9)
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
    print("\n-------------------------------------------------------------------------")
    print("                        WELCOME TO FEARNOT CENTRAL                       ")
    print("                            MY NAME IS",
          name, "                            ")
    print("          I WILL BE HERE TO HELP YOU ORDER FROM OUR SERVICES TODAY       ")
    print("-------------------------------------------------------------------------")

# Asks the user if the order is intended for click and collect or delivery


def order_type():
    '''
    Purpose: Prompts the user to select between home delivery or click & collect for their order and gathers the corresponding information.
    Parameters: None
    Returns: del_click: A string indicating the delivery option chosen ("delivery" for delivery, "click" for click & collect).
    '''
    del_click = ""  # Initializes a variable to store the delivery/click & collect information
    # Defines the question prompt for selecting delivery or click & collect
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("Do you want your order delivered or are you planning to click & collect?")
    print("To select delivery enter '1'")
    print("To select Click & Collect enter '2'")
    print("Please note that if delivery is selected, a $9 delivery charge will be added to total cost if 5 or less items are ordered otherwise delivery is free :)")
    # Prompts the user to enter a number between 1 and 2 to select delivery or click & collect
    delivery = val_int(LOW, HIGH, question)

    if delivery == 1:
        print("> You have chosen to have your order delivered to your door!")
        del_click = "delivery"  # Sets the delivery/click & collect variable to "delivery"
        delivery_info()  # Calls a function to begin gathering delivery information

    elif delivery == 2:
        print("> You have chosen to click and collect your order from our factories!")
        del_click = "click"  # Sets the delivery/click & collect variable to "click"
        click_collect_info()  # Calls a function to begin gathering click & collect information
    return del_click  # Returns the delivery/click & collect information


# Collects the user's name, address and phone number if order is intended for delivery
def delivery_info():
    '''
    Purpose: Collects the customer's name, phone number, house number, street name, and suburb for home delivery.
    Parameters: None
    Returns: None
    '''
    print("Please provide your name, phone number and address so we know where to send the merch to you!")
    # Basic instructions for asking name
    question = ("Please enter your name: ")
    # Asks for the customer's name and stores it in the customer_details dictionary under the 'name' key
    customer_details['name'] = check_string(question)
    print("> ", customer_details['name'])  # Prints the customer's name

    # Basic instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    # Asks for the customer's phone number and stores it in the customer_details dictionary under the 'phone' key
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # Prints the customer's phone number
    print("> ", customer_details['phone'])

    question = ("Please enter your house number: ")
    # Asks for the customer's house number and stores it in the customer_details dictionary under the 'house' key
    customer_details['house'] = not_blank(question)
    # Prints the customer's house number
    print("> ", customer_details['house'])

    question = ("Please enter your street name: ")
    # Asks for the customer's street name and stores it in the customer_details dictionary under the 'street' key
    customer_details['street'] = check_string(question)
    # Prints the customer's street name
    print("> ", customer_details['street'])

    question = (
        "Please enter your street type (Place, Drive, Ave, Street etc): ")
    # Asks for the customer's street name and stores it in the customer_details dictionary under the 'type' key
    customer_details['type'] = check_string(question)
    print("> ", customer_details['type'])  # Prints the customer's street type

    question = ("Please enter your suburb: ")
    # Asks for the customer's suburb and stores it in the customer_details dictionary under the 'suburb' key
    customer_details['suburb'] = check_string(question)
    print("> ", customer_details['suburb'])  # Prints the customer's suburb


# Collects the user's name and phone number if order was intended for click and collect
def click_collect_info():
    '''
    Purpose: Collects the customer's name and phone number for Click & Collect service.
    Parameters: None
    Returns: None
    '''
    # Asks the user to provide Click & Collect information (NAME AND PHONE NUMBER)
    print("Please provide your name and phone number so we know how to contact you!")

    # Basic instructions for asking name
    question = ("Please enter your name: ")
    # Asks for the customer's name and stores it in the customer_details dictionary under the 'name' key
    customer_details['name'] = check_string(question)
    print("> ", customer_details['name'])  # Prints the customer's name

    # Basic instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    # Asks for the customer's phone number and stores it in the customer_details dictionary under the 'phone' key
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # Prints the customer's phone number
    print("> ", customer_details['phone'])


def check_information(del_click):
    '''
    Purpose: Asks the user if the information they have entered is correct. If not, the program clears the necessary data and invokes the appropriate actions based on the user's choice.
    Parameters: del_click
    Returns: None
    '''
    print()
    # Prompt the user to enter a number between LOW and HIGH for confirmation
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    # Display the options to start another order or exit the bot
    print("Please confirm if the details you have entered are correct")
    if del_click == "click":
        print
        # Prints the customer's name and phone number
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}\nOrder type: Click & Collect")
    elif del_click == "delivery":  # Checks if the delivery option is "delivery"
        # Prints the customer's name, phone number, and address for delivery.
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['type']} {customer_details['suburb']} \nOrder type: Delivery")

    print("To confirm your details and proceed, enter 1")
    print("To reenter any of the above details, enter 2")
    # Validate the user's input to choose between starting another order or exiting the bot
    detailsconfirm = val_int(LOW, HIGH, question)
    if detailsconfirm == 1:
        print("Your details have been confirmed with us")
        print("*moves on to catalog*")
    elif detailsconfirm == 2:
        print("")
        # Clear the customer details dictionary
        customer_details.clear()
        del_click = ""
        main()


# Run the main function to start the program
main()
