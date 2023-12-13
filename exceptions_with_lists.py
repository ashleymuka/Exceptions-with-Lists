'''
Description: Write a program that outputs the name specified by the list index entered by the user

'''


names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']

index = int(input())


try:
    print(f'Name: {names[index]}')


except IndexError as error:
    print("Exception! list index out of range")

    if index < 0:
        print(f'The closest name is: {names[0]}')

    elif index > 0:
        print(f'The closest name is: {names[-1]}')

