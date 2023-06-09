#COMPONENT 6
# VERSION 4

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
    while True:
            try:
                num_merch = int(input("How many merch pieces would you like to order today?: "))
                if num_merch >= 1 and num_merch <= 15: 
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

        

# print order
print(order_list)
print(order_cost)

catalog()
order_merch()