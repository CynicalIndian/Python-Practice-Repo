while True:
    print('Enter the password')
    userInput = input()
    if(userInput != 'QWERTY123'):
        print('Inorrect Password')
        continue
    elif(userInput == 'QWERTY123'):
        print('Correct Password')
        break
