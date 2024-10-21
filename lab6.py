# Melissa Calixte
print ('Menu')
print('-------------')
print('1. Encode\n2. Decode\n3. Quit')

option = int(input('Please enter an option: '))
if option == 1:
    password = input('Please enter your passcode to encode: ')
    string = ""
    for i in password:
        i = int(i)
        i = i + 3
        if i >= 10:
            i = int(i - 10)
        string += str(i)
    print(string)

