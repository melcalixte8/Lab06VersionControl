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

def decoder(password):
    string = ""
    for i in password:
        i = int(i)
        i = i - 3
        if i <= 0:
            i = int(10 + i)
        string += str(i)
    return string

if __name__ == '__main__':
    password = "0"
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')

        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your passcode to encode: ')
            password = encoder(password)
            print(password)
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decoder(password)}.")
        elif option == 3:
            break
        print()
