#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number,
#Repeat asking the user until the random number has been guessed correctly.

import random

while True:
    rng = list(range(101))
    random.shuffle(rng)
    num = rng[0]
    while True:
        print('----------------------------------------')
        type = input('Type "C/c" for checking and "P/p" for playing: ')
        if type != 'C' and type != 'c' and type != 'P' and type != 'p':
            print('Type (C/P or c/p) only!')
        if type == 'C' or type == 'c' or type == 'P' or type == 'p':
            if type == 'C' or type == 'c':
                print()
                print(f'The mystery number is {num}')
                print()
                break
            elif type == 'P' or type == 'p':
                print()
                break
    print('----------------------------------------')
    print('GUESS THE NUMBER! :)')
    while True:
        invalid = 0
        hints = 0
        print('----------------------------------------')
        print('Type "00" to see hint!')
        guess = (input('Guess: '))
        print()
        if guess == '00':
            if num >= 0 and num < 11:
                hint = '(The mystery number is from 0-10)'
            elif num > 10 and num < 21:
                hint = '(The mystery number is from 11-20)'
            elif num > 20 and num < 31:
                hint = '(The mystery number is from 21-30)'
            elif num > 30 and num < 41:
                hint = '(The mystery number is from 31-40)'
            elif num > 40 and num < 51:
                hint = '(The mystery number is from 41-50)'
            elif num > 50 and num < 61:
                hint = '(The mystery number is from 51-60)'
            elif num > 60 and num < 71:
                hint = '(The mystery number is from 61-70)'
            elif num > 70 and num < 71:
                hint = '(The mystery number is from 71-80)'
            elif num > 80 and num < 81:
                hint = '(The mystery number is from 81-90)'
            elif num > 90 and num < 101:
                hint = '(The mystery number is from 91-100)'
            print(hint)
            hints = 1
        if not guess.isdigit():
            print('ERROR: Whole numbers only!')
            print('----------------------------------------')
        if guess.isdigit():
            guess = int(guess)
            if guess > 100 or guess < 0:
                print('ERROR: From 0-100 only!')
                invalid = 1
            if guess > num and invalid == 0:
                print(f'({guess} is > the mystery number!)')
            elif guess < num and invalid == 0 and hints == 0:
                print(f'({guess} is < the mystery number!)')
            elif guess == num:
                print('Your answer is correct!')
                print(f'The mystery number is {num}')
                print('----------------------------------------')
                break
    while True:
        restart = input('Try Again? Y/N: ')
        if restart != 'Y' and restart != 'N' and restart != 'y' and restart != 'n':
            print('(Y/N) or (y/n) only!')
        if restart == 'Y' or restart == 'N' or restart == 'y' or restart == 'n':
            break
    if restart == 'Y' or restart == 'y':
        continue
    elif restart == 'N' or restart == 'n':
        break
print()
print('----------------------------------------')
print('Thank you for playing!')
print('----------------------------------------')

            


            
        
        


            

