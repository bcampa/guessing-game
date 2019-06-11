# jogo da adivinhação
import random
import os

minimum = 0
maximum = 1000
playing = True
guessing = True
tries = 0


def clear():
    os.system('cls')


while playing:
    print(f'Guess the number (between {minimum} and {maximum})')
    number = random.randrange(minimum, maximum, 1)
    while guessing:
        while True:
            try:
                guess = int(input('Your guess: '))
                break
            except ValueError:
                print('Invalid input!')
                tries += 1
        if guess == number:
            print('Correct!')
            guessing = False
        elif guess > number:
            print('Too high.')
        elif guess < number:
            print('Too low.')
        tries += 1
    if tries < 10:
        print('Nicely done.')
    print(f'Number of tries: {tries}')
    while True:
        play_again = input('Would you like to play again? (Y/N)\n')
        play_again = play_again.upper()
        if play_again != 'Y' and play_again != 'N':
            print('Invalid input!')
        elif play_again == 'Y':
            guessing = True
            tries = 0
            clear()
            break
        elif play_again == 'N':
            playing = False
            break
