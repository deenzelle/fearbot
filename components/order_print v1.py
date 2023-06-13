# list to store ordered merch items
order_list = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)',]
# list to store ordered merch prices
order_cost = [69.50, 69.50, 69.50, 69.50]

cust_details = {'name': 'Denz', 'phone': '0211690403', 'house': '69', 'street': 'Tokki Drive', 'suburb': 'Flat Bush'}

count=0
for item in order_list:
    print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
    count = count + 1