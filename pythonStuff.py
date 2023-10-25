#import math

userInput = input()

# if (userInput == "test"):
#     print('You entered the word: "test"')

condition = True
while (condition):
    print('Enter a number, enter the number 5 to exit out of the application.')
    userInput = input()
    if (userInput == "5"):
        condition = False


print("successfully exited")

thisIsCamelCase = "camel case"
















# Function definition
#---------------------------------------------------------
# def addTwoNumbers(num1, num2):
#     addedNumbers = num1 + num2
#     return addedNumbers
# #---------------------------------------------------------

# sumOfTheTwoNumbers = addTwoNumbers(2, 3) # will equal 5
# print(sumOfTheTwoNumbers)
# number = 1

# while (number <= 100): # number == 11
#     for i in range(2, number): # will loop from 2 - 11
#         if (number % i == 0): #if the number / i has a remainder:
#             # This will be true if the number is composite
#             break
#     else:
#         print(number)
#     number += 1