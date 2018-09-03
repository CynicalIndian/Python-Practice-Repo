import sys
while  True:
    print('Hello youre stuck in a loop')
    print('You will die here, unless you type the password')
    userInput = input()
    if (userInput == 'IOPIOPIOP'):
        print('Got it correct Kiddo')
        sys.exit()
