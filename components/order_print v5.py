#Component 7
#V5

# list to store ordered merch items
order_list = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)',]
# list to store ordered merch prices
order_cost = [69.50, 69.50, 69.50, 69.50]

cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Flat Bush'}

def order_type():  # Defines a new function for the order type
    '''
    Purpose: To ask the user how they want their order to be prepared, Click & Collect or Delivery
    Parameters: None
    Returns: None
    '''
    del_click = ""
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
                    del_click = "delivery"
                    break  # Breaks out of loop to progress with program

                elif delivery == 2:  # Checks to see if the input entered is '2', if so, the program will print 'Click and Collect' then break out of loop
                    # If' '2' is inputted, the program will progress onto the click_collect() function
                    del_click = "click"
                    break  # Breaks out of loop to progress with program

            else:  # If the input was not one of those two, the program will print this message
                # Clearly states what the user has to enter to proceed with their order
                print("Please pick between 1 (Delivery) or 2 (Click and Collect)")

        except ValueError:  # If input = ValueError, prints following error message
            # Only allows numbers to be a valid input
            print("That is not a valid number")
            # Clearly states what the user has to enter to proceed with their order
            print("Please pick between 1 (Delivery) or 2 (Click and Collect)")
    return del_click

def print_order(del_click):
    print()
    total_cost = sum(order_cost)
    print("Customer Details:")
    if del_click == "click":
        print("Your order is will be available for Click and Collect soon!")
        print(f"Customer Name: {cust_details['name']} \nCustomer Phone Number: {cust_details['phone']}")
    elif del_click == "delivery":
        print("Your order will be delivered to you!")
        print(f"Customer Name: {cust_details['name']} \nCustomer Phone Number: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    count=0
    print()
    print("Items in Cart:")
    for item in order_list:
        print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count + 1

    print()
    print("Order Cost Details:")
    print(f"The total cost of the order is: ${total_cost:.2f}")

def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    order_type()
    del_click = order_type()
    print_order(del_click)


main()  # Runs the main function
