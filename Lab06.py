def encode(password):  # function to encode password
    encoded_password = ""  # sets empty str variable to store encoded password
    for digit in password:  # for loop to iterate through each digit
        digit = int(digit)  # converts digit into an int to use math on it
        digit += 3  # adds 3 to digit to encode it
        if digit >= 10:  # used to limit the digit to be between 0 and 9 if the digit it greater than or equal to 10
            digit -= 10  # subtracts by 10. If digit is 8, and it adds 3, it'll be 11, but it should be 1
        digit = str(digit)  # converts digit to a string to then add it to the empty str variable
        encoded_password += digit
    return encoded_password


def decode(password):
    pass


def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original is {decoded_password}.\n")
        elif option == 3:
            break


if __name__ == '__main__':
    main()