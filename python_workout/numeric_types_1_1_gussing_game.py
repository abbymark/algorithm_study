import random

def guessing_game():
    random_int = random.randint(0, 100)
    count = 0
    while True:
        guessed_int = int(input('Guess a number:'))
        if guessed_int > random_int:
            print('Too high')
            count += 1
        elif guessed_int < random_int:
            count += 1
            print('Too low')
        else:
            print('Just right')
            break

        if count > 2:
            print('You did not succeed')
            break

guessing_game()