# Ask user if they want to generate the password or not
# if yes, ask for password length
# generate password
# print the password
# if no, exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a random password? (Yes/No) > ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Exiting the program...")
    quit()
else:
    print("Invalid input, please enter (Yes/No) > ")
    quit()