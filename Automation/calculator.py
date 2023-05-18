# define the functions needed: +, -, *, /
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until user want to exit

def add(x, y):
    answer = x + y
    print(str(x) + " + " + str(y) + " = " + str(answer) + "\n")

def sub(x, y):
    answer = x - y
    print(str(x) + " - " + str(y) + " = " + str(answer) + "\n")

def mul(x, y):
    answer = x * y
    print(str(x) + " * " + str(y) + " = " + str(answer) + "\n")

def div(x, y):
    answer = x / y
    print(str(x) + " / " + str(y) + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice > ")

    match choice:
        case "a" | "A":
            print("Addition")
            x = int(input("Enter first number > "))
            y = int(input("Enter second number > "))
            add(x, y)
        case "b" | "B":
            print("Subtraction")
            x = int(input("Enter first number > "))
            y = int(input("Enter second number > "))
            sub(x, y)
        case "c" | "C":
            print("Multiplication")
            x = int(input("Enter first number > "))
            y = int(input("Enter second number > "))
            mul(x, y)
        case "d" | "D":
            print("Division")
            x = int(input("Enter first number > "))
            y = int(input("Enter second number > "))
            div(x, y)
        case "e" | "E":
            print("Exiting the program...")
            quit()



