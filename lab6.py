# Melissa Calixte
def encoder(password):
    string = ""
    for i in password:
        i = int(i)
        i = i + 3
        if i >= 10:
            i = int(i - 10)
        string += str(i)
    return string

if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your passcode to encode: ')
            password = encoder(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            pass

        elif option == 3:
            break








