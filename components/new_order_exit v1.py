# Component 9
# V1

print("Please confirm your order")
print("To confirm your order, enter 1")
print("To cancel your order, enter 2")

while True:
    try:
        confirm = int(input("Please enter a number: "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("Your merch order has been confirmed!")
                print("Your merch order will be with you soon!")
                break

            elif confirm == 2:
                print("Your merch order has been cancelled")
                print("You can restart your merch order or exit the BOT")
                break
        else:
            print("The number must be 1 or 2")

    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")