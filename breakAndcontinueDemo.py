while True:
    print('Enter the password')
    userInput = input()
    if(userInput != 'QWERTY123'):
        print('Inorrect Password')
        continue
    elif(userInput == 'QWERTY123'):
        print('Correct Password')
        break
for i in range(0,11):
    print (i)
    if(i==5):
        break
print('')
for j in range(0,11):
    print(j)
    if(j==10):
        continue
