# COMPONENT 4
# VERSION 2

# customer details dictionary
customer_details = {}

# defines a not blank variable


def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")


def delivery():
    # Basic instructions for asking name
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    # Basic instructions for asking for user's phone number
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])


delivery()
