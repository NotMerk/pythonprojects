import pywhatkit

def menu():
    print("[1] Direct Message (Instant)")
    print("[2] Direct Message (Schedule)")
    print("[3] Group Message (Instant)")
    print("[4] Group Message (Schedule)")
    print("[0] Exit")

def option1():
    phone_number = input("Enter phone number > ")
    dm_message = input("Enter message > ")

    pywhatkit.sendwhatmsg_instantly(phone_number, dm_message)

def option2():
    phone_number = input("Enter phone number > ")
    dm_message = input("Enter message > ")
    hr = int(input("Enter hour (24-hour) > "))
    min = int(input("Enter minutes (24-hour) > "))

    pywhatkit.sendwhatmsg(phone_number, dm_message, hr, min)

def option3():
    group_id = input("Enter group ID > ")
    group_message = input("Enter message > ")
    
    pywhatkit.sendwhatmsg_to_group_instantly(group_id, group_message)

def option4():
    group_id = input("Enter group ID > ")
    group_message = input("Enter message > ")
    hr = int(input("Enter hour (24-hour) > "))
    min = int(input("Enter minutes (24-hour) > "))
    
    pywhatkit.sendwhatmsg_to_group(group_id, group_message, hr, min)

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    else:
        print("Invalid option.")
    
    menu()
    option = int(input("Enter your option: "))

print("Goodbye, come again!")







