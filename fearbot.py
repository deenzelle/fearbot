# FEARBOT Program
# A progam that can be used by 'FEARNOT' to order LE SSERAFIM merch
# dealing with comments when the internal is finished

# Imports a library that allows the program to have randomness where nescessary
import random
from random import randint  # Imports the ability to choose between integers randomly

# Creates the customer detail dictionary to have memory of user input of details
customer_details = {}

# List of names
names = ["Kazuha", "Chaewon", "Nicole", "Kaitlin", "Denzelle",
         "Yunjin", "Eunchae", "Jaehyun", "Jungkook", "Sakura"]

# list of merchandise items available to purchase
merch_names = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)', 'ANTIFRAGILE ALBUM (IRIDESCENT OPAL VER)', 'ANTIFRAGILE ALBUM (MIDNIGHT ONYX VER)',
               'UNFORGIVEN ALBUM (DEWY SAGE VER)', 'UNFORGIVEN ALBUM (DUSTY AMBER VER)', 'UNFORGIVEN ALBUM (BLOODY ROSE VER)', 
               'LE SSERAFIM LIGHT STICK', 'LE SSERAFIM FLOOR MAT', 'LE SSERAFIM TUMBLER', 'LE SSERAFIM HOODIE']

# list of available merchandise prices
merch_prices = [69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 45.50, 25.50, 15.50, 45.50]

# Defines a function called not_blank, validates inputs to check if they are blank
def not_blank(question):
    '''
    Purpose: Checks input to make sure it is not blank, if blank
    it will ask the user to input something that is not blank
    Parameters: Question
    Returns: Response
    '''
    valid = False
    while not valid:  # If not valid
        # Because there isn't a set question, this function will be able to work with any question = x variable
        response = input(question)
        if response != "":
            # Returning the response also breaks loop, .title changes strings to make it a capital
            return response.title()
        else:
            # Clear instructions
            print("The input you provide cannot be blank")

# Defines a welcome function that welcomes the customer to the bot


def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
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
    print("*** Welcome to FEARNOT Central")
    print("*** My name is", name)  # Prints out the randomly selected name
    print("*** I will be to help you order OFFICIAL LE SSERAFIM MERCHANDISE")

# Asks the user if the order is intended for click and collect or delivery


def order_type():  # Defines a new function for the order type
    '''
    Purpose: To ask the user how they want their order to be prepared, Click & Collect or Delivery
    Parameters: None
    Returns: None
    '''
    # Asks the user how they would prefer to have their order handled
    print("Do you want your order delivered or are you planning to click & collect?")
    # Clearly states what the user has to enter to proceed with their order
    print("To select delivery enter '1'")
    # Clearly states what the user has to enter to proceed with their order
    print("To select Click & Collect enter '2'")
    while True:  # Creates a loop where while it is 'True', the program will continually ask the user to input either 1 or 2
        try:
            # Sets the delivery variable to the integer inputted (ideally it should be either 1 or 2)
            delivery = int(input())
            if delivery >= 1 and delivery <= 2:  # Checks to see if the number is greater than or equal to 1, or less than or equal to 2
                if delivery == 1:  # Checks to see if the input entered is '1', if so, the program will print 'Delivery' then break out of loop
                    delivery_info()
                    break  # Breaks out of loop to progress with program

                elif delivery == 2:  # Checks to see if the input entered is '2', if so, the program will print 'Click and Collect' then break out of loop
                    # If' '2' is inputted, the program will progress onto the click_collect() function
                    click_collect_info()
                    break  # Breaks out of loop to progress with program

            else:  # If the input was not one of those two, the program will print this message
                # Clearly states what the user has to enter to proceed with their order
                print("Please pick between 1 (Delivery) or 2 (Click and Collect)")

        except ValueError:  # If input = ValueError, prints following error message
            # Only allows numbers to be a valid input
            print("That is not a valid number")
            # Clearly states what the user has to enter to proceed with their order
            print("Please pick between 1 (Delivery) or 2 (Click and Collect)")


# Collects the user's name, address and phone number if order is intended for delivery
def delivery_info():
    # Basic instructions for asking name
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    # print(customer_details['name'])

    # Basic instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    # print(customer_details['phone'])

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    # print(customer_details['house'])

    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question)
    # print(customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    # print(customer_details['suburb'])


# Collects the user's name and phone number if order was intended for click and collect
def click_collect_info():
    # Asks the user to provide Click & Collect information (NAME AND PHONE NUMBER)
    print("You have chosen to have our Click & Collect service")
    print("Please provide your name and phone number so we know how to contact you!")
    # Basic instructions for asking name
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    # print (customer_details['name'])

    # Basic instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    # print (customer_details['phone'])

# Make a menu of at least 12 items for the user to choose from
# Make each item available item orderable
# Make the cost of each item display within the menu
def catalog():
    number_merch = 13
    for count in range (number_merch):
        print("{} {} ${:.2f}" .format(count+1,merch_names[count],merch_prices[count]))

# Prints out order details
# Items & Prices
# Total cost of order, incl delivery charge (if applicable)
# Customer's name
# Customer's phone number
# (IF ORDER IS FOR DELIVERY) Print out customer's address

# Asks the user if they wish to cancel the order before submitting it

# Ask if user wishes to place another order, or exit the bot
# if order is for pickup, notify the user that they will receive a text message when order is ready once confirmed

# Calls the function/Tells the program to run a specific function


def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()
    order_type()
    catalog()


main()  # Runs the main function
