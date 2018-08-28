#This is a program to demonstrate how a for loop works in python.
#The program will print the multiplication table of a number which is taken from the user
print('Enter a number please.')
userInput = int(input())
print ('The Table is:')
for i in range (0, 11):
    print(str(userInput * i))
