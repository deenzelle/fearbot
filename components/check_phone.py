# phone number validation string
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        num = input(question)  # Prompt the user to enter a phone number
        if num.isdigit():  # Check if the input consists only of digits
            count = len(num)  # Calculate the length of the input
            if count >= PH_LOW and count <= PH_HIGH:  # Check if the length is within the desired range
                return num  # Return the phone number as a string
            else:
                print("NZ phone numbers have between 7 and 10 digits")  # Display an error message if the length is not within the desired range
        else:
            print("Please only enter integers!")  # Display an error message if the input is not composed of digits

question = "Please enter your phone number: "
PH_LOW = 7
PH_HIGH = 10

phone = check_phone(question, PH_LOW, PH_HIGH)
print(phone)
