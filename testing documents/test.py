def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        num = input(question)
        if num.isdigit():
            count = len(num)
            if count >= PH_LOW and count <= PH_HIGH:
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        else:
            print("Please only enter integers!")

question = "Please enter your phone number: "
PH_LOW = 7
PH_HIGH = 10

phone = check_phone(question, PH_LOW, PH_HIGH)
print(phone)