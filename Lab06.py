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


def decode(password):  # function decodes password
    decoded_password = ""  # creates open string for later addition of integers
    for digit in password:
        digit = int(digit)  # turns digit into digit for subtraction
        digit -= 3  # removes encoded change by subtracting 3
        if digit < 0:  # if number results in a negative number, add 10 to get original encoded digit (positive value)
            digit += 10
        digit = str(digit)  # turns back into string
        decoded_password += digit  # adds digit in string form to decoded_ password string
    return decoded_password


def main():
    while True:
        print("Menu\n"  # prints menu
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))  # variable to store menu selection
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))  # immediately encodes the input, and stores it as a variable
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded_password = decode(encoded_password)  #  if option 2 is chosen, run decode function and store into variable
            print(f"The encoded password is {encoded_password}, and the original is {decoded_password}.\n")  # f string print with respective variables
        elif option == 3:  # quit program
            break


if __name__ == '__main__':
    main()