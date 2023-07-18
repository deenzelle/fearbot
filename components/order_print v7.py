#component 7

#Component 7
#V6

customer_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'type': 'among', 'suburb': 'Flat Bush'}

# list of merchandise items available to purchase
merch_names = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)', 'ANTIFRAGILE ALBUM (IRIDESCENT OPAL VER)', 'ANTIFRAGILE ALBUM (MIDNIGHT ONYX VER)',
               'UNFORGIVEN ALBUM (DEWY SAGE VER)', 'UNFORGIVEN ALBUM (DUSTY AMBER VER)', 'UNFORGIVEN ALBUM (BLOODY ROSE VER)', 
               'LE SSERAFIM LIGHT STICK', 'LE SSERAFIM FLOOR MAT', 'LE SSERAFIM TUMBLER', 'LE SSERAFIM HOODIE']

# list of available merchandise prices
merch_prices = [69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 45.50, 25.50, 15.50, 45.50]

# list to store ordered merch items
order_list = []
# list to store ordered merch prices
order_cost = []

#Create pizza menu
def catalog():
    number_merch = 13
    for count in range (number_merch):
        print("{} {} ${:.2f}" .format(count+1,merch_names[count],merch_prices[count]))

def order_merch():
    # ask for the total amount of merchandise for order
    num_merch = 0

    # Creates a while true loop to make sure that integer is valid and not a value error
    # Creates a while true loop to make sure that integer is valid and not a value error
    while True:
            try:
                num_merch = int(input("How many merch pieces would you like to order today?: "))
                if num_merch >= 1 and num_merch <= 5: 
                    break
                elif num_merch >= 6 and num_merch <= 15:
                    break
                else:
                    print("Please only choose between 1 and 15 merch items to order")

            except ValueError:
                print("That is not a valid number")
                print("Please pick between bigger than 1")    
    print(num_merch)
    
    # Choose merch item from menu
    for item in range(num_merch):
        while num_merch > 0:
            while True:
                try:
                    merch_ordered = int(input("Please choose your merchandise items by entering the number on the menu: "))
                    if merch_ordered >= 1 and merch_ordered <= 13:
                        break
                    else:
                        print("Please make sure you choose an available item that is listed above between 1-13")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 13")

            merch_ordered = merch_ordered - 1
            order_list.append(merch_names[merch_ordered])
            order_cost.append(merch_prices[merch_ordered])
            num_merch = num_merch - 1
            print("{} ${:.2f}" .format(merch_names[merch_ordered],merch_prices[merch_ordered]))

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
    print("Please note that if delivery is selected, a $9 delivery charge will be added to total cost if 5 or less items are ordered")
    print("otherwise delivery is free :)")
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
    count = 0
    delivery_cost = 0 
    if del_click == "delivery":
        if len(order_list) < 5:
            print("It seems your order has 4 or less items in the cart, a $9 delivery charge will be applied")
            delivery_cost = 9
            print()
        else:
            delivery_cost = 0 
             
    print("\n--------------------------------------------------")
    print("                   ORDER RECEIPT                   ")
    print("--------------------------------------------------")
    print("Customer Details:")
    if del_click == "click":
        print("Delivery Option: Click & Collect")
        print(f"Customer Name: {customer_details['name']}")  # Prints the customer's name
        print(f"Customer Phone Number: {customer_details['phone']}")  # Prints the customer's phone number
    elif del_click == "delivery":
        print("Delivery Option: Delivery")
        print(f"Customer Name: {customer_details['name']}")  # Prints the customer's name
        print(f"Customer Phone Number: {customer_details['phone']}")  # Prints the customer's phone number
        print(f"Customer Address: {customer_details['house']} {customer_details['street']} {customer_details['type']}")
        print(f"                  {customer_details['suburb']}")  # Prints the customer's address
    
    print("--------------------------------------------------")
    print("Items in Cart:")
    
    for item in order_list:
        # Prints the ordered item and its corresponding cost
        print("{}  ${:.2f}" .format(item, order_cost[count]))
        # Increments the counter variable for the next iteration.
        count = count + 1

    print("--------------------------------------------------")
    subtotal = sum(order_cost)  # Calculates the subtotal by summing all the costs
    total_cost = subtotal + delivery_cost
    print(f"Subtotal:                      ${subtotal:.2f}")  # Prints the subtotal
    print(f"Delivery Charge:               ${delivery_cost:.2f}")  # Prints the delivery charge
    total_cost = subtotal + delivery_cost  # Calculates the total cost
    print(f"Total:                         ${total_cost:.2f}")  # Prints the total cost
    print("--------------------------------------------------")

def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    del_click = order_type()
    catalog()
    order_merch()
    print_order(del_click)


main()  # Runs the main function
