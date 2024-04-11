#Andres Soto Encoder File
#Decoder by Patrick Leimer
def encoder(string):
    if string.isnumeric():
        encoded_string = ""
        for char in string:
            digit = int(char)
            digit = (digit + 3) % 10
            encoded_string += str(digit)
        return encoded_string
def decoder(encondedPassword):
    decodedPass = ''
    for num in encondedPassword:
        if (int(num)) < 3:
            decodedPass += str(10 - (int(num) - 3))
        else:
            decodedPass += str(int(num) - 3)
    return decodedPass
def main():
    password = ''
    while True:
        print("""\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit""")
        option = input("Please Enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isnumeric():
                password = encoder(password)
                print("Your password has been encoded and stored!")
            else:
                print("Error! Enter 8 digit password")
        #Patrick ->
        if option == "2":
            originalPassword = decoder(list(password))
            print(f"The encoded password is {password}, and the original password is {originalPassword}.")

        if option == "3":
            break
if __name__ == "__main__":
    main()
