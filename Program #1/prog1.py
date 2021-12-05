#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.
import sys
import random


while True:
    rng = list(range(10))
    random.shuffle(rng)
    num1 = rng[0]
    num2 = rng[1]
    num3 = rng[3]
    while True:
        type = input('Type "C/c" for checking and "P/p" for playing: ')
        if type != 'C' and type != 'c' and type != 'P' and type != 'p':
            print('Type (C/P or c/p) only!')
        if type == 'C' or type == 'c' or type == 'P' or type == 'p':
            if type == 'C' or type == 'c':
                print()
                print(f'The random numbers are {num1}, {num2}, and {num3}.')
                print()
                break
            elif type == 'P' or type == 'p':
                print()
                break
    print('First Guess?')
    while True:
        guess1 = (input('Guess#1: '))
        print()
        if not guess1.isdigit():
            print('Whole numbers only!')
        if guess1.isdigit():
            guess1 = int(guess1)
            if guess1 > 9 or guess1 < 0:
                print('From 0-9 only!')
            else:
                break
    print('Second Guess? ')
    while True:
        guess2 = (input('Guess#2: '))
        print()
        if not guess2.isdigit():
            print('Whole numbers only!')
        if guess2.isdigit():
            guess2 = int(guess2)
            if guess2 > 9 or guess2 < 0:
                print('From 0-9 only!')
            else:
                break
    print('Third guess? ')
    while True:
        guess3 = (input('Guess#3: '))
        print()
        if not guess3.isdigit():
            print('Whole numbers only!')
        if guess3.isdigit():
            guess3 = int(guess3)
            if guess3 > 9 or guess3 < 0:
                print('From 0-9 only!')
            else:
                break    

    guess1 = int(guess1)
    guess2 = int(guess2)
    guess3 = int(guess3)
    g1score = 0
    g2score = 0
    g3score = 0
    if guess1 == num1 or guess1 == num2 or guess1 == num3:
        g1score = 1
        if guess1 == guess2:
            g1score = 0
        elif guess1 == guess3:
            g1score = 0 
    if guess2 == num1 or guess2 == num2 or guess2 == num3:
        g2score = 1
        if guess2 == guess1:
            g1score = 0
        elif guess2 == guess3:
            g1score = 0 
    if guess3 == num1 or guess3 == num2 or guess3 == num3:
        g3score = 1
        if guess3 == guess2:
            g1score = 0
        elif guess3 == guess1:
            g1score = 0 
    score = (g1score + g2score + g3score)
    if score == 3:
        print('Winner!')
        print()
    else:
        print('You lose!')
        print()
        print('The correct numbers are: ')
        print(f'{num1}, {num2}, {num3}')
        print()
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
print('Thank you for playing!')
sys.exit
