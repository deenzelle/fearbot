# COMPONENT 3
# VERSION 2

# Notes:
# - Find a better way of storing name and phone number
# - Not valid (variable) is repeated
# - Name allows integer inputs
# - Phone number allows letter inputs

print("Please enter the Click & Collect information")

valid = False
while not valid:
    # customer name
    name = input("Please enter your name: ")
    if name != "":
        print(name)
        break
    else:
        print("Sorry this cannot be blank")
        
valid = False
while not valid:    
    # customer phone number
    phone = input("Please enter your phone number: ")
    if phone != "":
        print(phone)
        break
    else:
        print("Sorry this cannot be blank")

print(name)
print(phone)