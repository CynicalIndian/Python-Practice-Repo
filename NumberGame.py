userInput = 0 #userInput value has been set to 0 by default
userChoice = 'u'  #userChoice value has been set to undefined or u
contu = True    #contu value by default is set to true
while contu == True:
    print ('Welcome to number games.')
    print ('Enter a number, and if it is even, You win.')
    userInput = int(input())
    if(userInput % 2 == 0):
        print('You win')
    else:
        print('I win')
    print('Do you wish to play again')
    userChoice = input()
    if((userChoice == 'Y') or (userChoice == 'y ')):
        contu = True
    elif((userChoice == 'N') or (userChoice == 'n')):
        contu = False
    else:
        print('Invalid input, you will play again')
        contu = True
