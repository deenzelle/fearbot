#component numero 6
# list of merchandise items available to purchase
pizza_names = ['FEARLESS ALBUM (BLACK PETROL VER)', 'FEARLESS ALBUM (MONOCHROME BOUQUET VER)', 'FEARLESS ALBUM (BLUE CYPHER VER)',
               'ANTIFRAGILE ALBUM (FROZEN AQUAMARINE VER)', 'ANTIFRAGILE ALBUM (IRIDESCENT OPAL VER)', 'ANTIFRAGILE ALBUM (MIDNIGHT ONYX VER)',
               'UNFORGIVEN ALBUM (DEWY SAGE VER)', 'UNFORGIVEN ALBUM (DUSTY AMBER VER)', 'UNFORGIVEN ALBUM (BLOODY ROSE VER)', 
               'LE SSERAFIM LIGHT STICK', 'LE SSERAFIM FLOOR MAT', 'LE SSERAFIM TUMBLER', 'LE SSERAFIM HOODIE']

# list of available merchandise prices
pizza_prices = [69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 69.50, 45.50, 25.50, 15.50, 45.50]

# list to store ordered pizzas
order_list = []
# list to store ordered pizzas prices
order_cost = []

#Create pizza menu
def menu():
    number_pizzas = 13
    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count]))


def order_pizza():
    # ask for the total amount of pizzas for order
    num_merch = 0

    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order?: "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5 pizzas")
        except ValueError:
            print("That is not a valid number")
            print("Please choose a number between 1 and 5")

    print(num_pizzas)

    # Choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please choose your pizzas by entering the number on the menu: "))
                    if  ed >= 1 and pizza_ordered <= 13:
                        break
                    else:
                        print("Your pizza order must be between 1 and 12 pizzas")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")

            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            num_pizzas = num_pizzas-1
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
        
menu()
order_pizza()