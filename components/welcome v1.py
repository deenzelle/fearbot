# COMPONENT 1
# VERSION 1

# Imports a library that allows the program to have randomness where nescessary
import random
from random import randint # Imports the ability to choose between integers randomly

# List of names
names = ["Hanni", "Chaewon", "Nicole", "Kaitlin", "Denzelle", "Harry", "Yeonjun", "Jaehyun", "Jungkook", "Sunghoon"]

# Chooses a random integer between 0 and 9
num = randint(0,9)

# Sets the name variable equal to the name which corresponds to the above selected integer
name = (names[num])

# Prints out basic welcome message
print("*** Welcome to FEARNOT Central")
print("*** My name is" ,name) # Prints out the randomly selected name
print("*** I will be to help you order OFFICIAL LE SSERAFIM MERCHANDISE")