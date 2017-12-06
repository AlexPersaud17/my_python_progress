def main():
    valid_password = False
    while not valid_password:
        print("\nPassword rules:")
        print("1. Should be at least 6 characters long and no more than 20 characters.")
        print("2. Should include a mix of upper and lower case letters.")
        print("3. Should include at least one digit.")
        password = input("Password: ")
        if len(password) >= 6 and len(password) <=20 and not password.isupper() and not password.islower() and not password.isalpha() and not password.isdigit() and password.isalnum():
            valid_password = True
            print("Password accepted!")
        else:
            print("Password not according to the rules.")
    
# main()

def main2():
    valid_password = False
    while not valid_password:
        print("\nPassword rules:")
        print("1. Should be at least 6 characters long and no more than 20 characters.")
        print("2. Should include a mix of upper and lower case letters.")
        print("3. Should include at least one digit.")
        password = input("Password: ")

        has_upper = False
        has_lower = False
        has_digit = False

        if password.isalnum() and len(password) <= 20 and len(password) >= 6:
            for letter in password:
                if letter.isupper():
                    has_upper = True
                if letter.islower():
                    has_lower = True
                if letter.isdigit():
                    has_digit = True

        if has_upper and has_lower and has_digit:
            valid_password = True
            print("Password accepted!")
        else:
            print("Password not according to the rules.")

main2()