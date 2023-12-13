'''
Author: Ashley Muka
Assignment Tilte:Exceptions with lists
Assignment Description: Write a program that outputs the name specified
by the list index entered by the user
Due Date: 09/11/2023
Date Created: 09/11/2023
Date Last Modified: 09/11/2023

'''

#input
names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']

index = int(input())

#process and output
try:
    print(f'Name: {names[index]}')

#process and output
except IndexError as error:
    print("Exception! list index out of range")

    if index < 0:
        print(f'The closest name is: {names[0]}')

    elif index > 0:
        print(f'The closest name is: {names[-1]}')

