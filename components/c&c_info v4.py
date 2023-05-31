# COMPONENT 3
# VERSION 4

# Creates the customer detail dictionary to have memory of user input of details
customer_details = {}

# Defines a function called not_blank
def not_blank(question):
    '''
    Purpose: Checks input to make sure it is not blank, if blank
    it will ask the user to input something that is not blank
    Parameters: Question
    Returns: Response
    '''
    valid = False
    while not valid:
        response = input(question) # Because there isn't a set question, this function will be able to work with any question = x variable
        if response != "":
            return response # Returning the response also breaks loop
        else:
            print("The input you provide cannot be blank")

# Asks the user to provide Click & Collect information (NAME AND PHONE NUMBER)
print("You have chosen to have our Click & Collect service")
print("Please provide your name and phone number so we know how to contact you!")

# Basic instructions for asking name
question = ("Please enter your name: ")
customer_details['name'] = not_blank(question)
print (customer_details['name'])

# Basic instructions for asking for user's phone number
question = ("Please enter your phone number: ")
customer_details['phone'] = not_blank(question)
print (customer_details['phone'])