import string
import re

valid = re.compile(r'[a-zA-Z]+')
print('------------ GREETINGS ------------')

name = input('\nPlease enter your name: ')

while not valid.match(name):
    print('Invalid characters!\n')
    name = input('Please enter your name: ')

print('\nChose language:\n\n1) English\n2) IsiXhosa\n3) Afrikaans')

while True:
    try:
        language = int(input('\nChoice: '))
        break
    except ValueError:
        print('Please enter a number between 1 and 3.')
        
if language == 1:
    print('\nHello, ' + name + '.\n')
elif language == 2:
    print('\nMolo, ' + name + '.\n')
elif language == 3:
    print('\nHallo, ' + name + '.\n')
else: 
    print('\nInvalid input')
    
print('------------ GOODBYE ------------')

