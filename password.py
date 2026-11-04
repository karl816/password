
# creating a password

while True:
    password = input("Create a password: ")
    if not password[0].isupper():
        print("The first letter must be uppercased")
    elif len(password) < 5:
        print("The password must have at least 5 characters.")
    elif not password.isalnum():
        print("The password must contain numbers and letters")
    else:
        print(f"Password created !")