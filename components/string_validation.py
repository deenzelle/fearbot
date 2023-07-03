#component 11??
# checks to see in string is valid

def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters")
        else:
            print(response.title())
            break
        
question = "please enter your name"
name = check_string(question)