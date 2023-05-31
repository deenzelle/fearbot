# COMPONENT 3
# VERSION 3

# Creates the customer detail dictionary to have memory of user input of details
customer_details = {}

# basic instructions
print("Please enter the Click & Collect information")
# custommer name not blank
valid = False
while not valid:
    # customer name
    customer_details[name] = input("Please enter your name: ")
    if customer_details[name] != "":
        print(customer_details[name])
        break
    else:
        print("Sorry this cannot be blank")
      
# customer phone not blank  
valid = False
while not valid:    
    # customer phone number
    customer_details[phone] = input("Please enter your phone number: ")
    if customer_details[phone] != "":
        print(customer_details[phone])
        break
    else:
        print("Sorry this cannot be blank")

print(name)
print(phone)