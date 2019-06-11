#jogo da adivinhação
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
    guess = int(maximum / 2)
    upper_limit = maximum
    lower_limit = minimum
    number = random.randrange(minimum, maximum, 1)
    while guessing:
        if guess == number:
            print(f'{guess} - Correct!')
            guessing = False
        elif guess > number:
            upper_limit = guess
            print(f'{guess} - Too high.')
            guess = int(lower_limit + (upper_limit - lower_limit) / 2)
        elif guess < number:
            lower_limit = guess
            print(f'{guess} - Too low.')
            guess = int(lower_limit + (upper_limit - lower_limit) / 2)
        tries += 1
    print(f'Number of tries: {tries}')
    while True:
        play_again = input('Play again? (Y/N)\n')
        play_again = play_again.upper()
        if play_again != 'Y' and play_again != 'N':
            print('Invalid input!')
        elif play_again == 'Y':
            guessing = True
            tries = 0
            guess = int(maximum / 2)
            upper_limit = maximum
            lower_limit = minimum
            clear()
            break
        elif play_again == 'N':
            playing = False
            break
