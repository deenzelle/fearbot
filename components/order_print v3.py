#Component 7
#V3

# list to store ordered merch items
order_list = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)',]
# list to store ordered merch prices
order_cost = [69.50, 69.50, 69.50, 69.50]

cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Flat Bush'}

#print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House Number: {} \nCustomer Street Name: {} \nCustomer Suburb: {}".format(cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb'],))
print(f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")

count=0
for item in order_list:
    print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count + 1