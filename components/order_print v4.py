#Component 7
#V4

# list to store ordered merch items
order_list = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)',]
# list to store ordered merch prices
order_cost = [69.50, 69.50, 69.50, 69.50]

cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Flat Bush'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details:")
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

print_order()