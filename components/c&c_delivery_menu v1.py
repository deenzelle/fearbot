# COMPONENT 2
# VERSION 1

# Bugs
# Will only work for valid input 'd' and 'p'

print("Do you want your order delivered or are you planning to click & collect?")

print("To select delivery enter 'd', to select Click & Collect enter 'c'")

delivery = input()

if delivery == "d":
    print ("delivery")
elif delivery == "c":
    print("click and collect")