# My name is Cole Jank, lab partner: Justin Williamson

def encode(password):
    encoded_password = ''
    for i in password:
        if int(i) <= 6:
            encoded_password += str(int(i) + 3)
        else:
            encoded_password += str(int(i) - 7)
    return encoded_password

def decode(password):
    converted_string = ''
    for i in password:
        if int(i) >= 3:
            converted_string += str(int(i) - 3)
        else:
            converted_string += str(int(i) + 7)

    return converted_string


def main():
    menu_option = True
    encoded_pw = ''
    original_pw = ''
    while menu_option:

        print("Password Menu: ")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")
        menu_option = int(input("Select a menu option: "))
        if menu_option == 1:
            password = input("Enter password to encode: ")
            encoded_pw = encode(password)
            print("Success! Your encoded password has been stored.")
        if menu_option == 2:
            original_pw = decode(encoded_pw)
            print(f'The encoded password is {encoded_pw}, and the original password is {original_pw}')
        if menu_option == 3:
            exit()
        else:
           print("Invalid menu option.")


if __name__ == '__main__':
    main()