#COMPONENT 6
# VERSION 2

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

catalog()

# ask for the total amount of merchandise for order
num_merch = 0

# Creates a while true loop to make sure that integer is valid and not a value error
while True:
        try:
            num_merch = int(input("How many merch pieces would you like to order today?: "))
            if num_merch >= 1: 
                    break
            else:
                print("Please enter a number bigger than 1")

        except ValueError:
            print("That is not a valid number")
            print("Please pick between bigger than 1")

# Choose merch item from menu
print("Please choose the merch by entering the number from the catalog menu")
for item in range(num_merch):
    while num_merch > 0:
        merch_ordered = int(input())
        order_list.append(merch_names[merch_ordered])
        order_cost.append(merch_prices[merch_ordered])
        num_merch = num_merch-1
        
print(order_list)
print(order_cost)
        
# Countdown until all pizzas are ordered

# print order