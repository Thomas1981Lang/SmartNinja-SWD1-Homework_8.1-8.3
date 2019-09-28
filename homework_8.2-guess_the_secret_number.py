import random

print('Gamemode: easy, normal, hard')
mode = input('Choose Gamemode: ')  # easy, normal, hard


if mode == 'easy':
    print('Debug easy')  # Debug
    hard_code_number = 42
    guess = int(input('Guess Secret Number: '))

    if guess == hard_code_number:
        print('Congratulation')
    else:
        print('Sorry Wrong Guess')

elif mode == 'normal':
    print('Debug normal')  # Debug
    input_number = int(input('Input Secret Number!: '))
    guess = int(input('Guess Secret Number: '))

    if input_number == guess:
        print('Congratulation')
    else:
        print('Sorry Wrong Guess')

elif mode == 'hard':
    print('Debug hard')  # Debug
    max_range = int(input('How much money do you want to win?: '))
    max_try = 5
    attempt = 1
    secret_number = random.randint(1, max_range)
    guess_txt = 'Guess Secret Number between 1 - ' + str(max_range) + ': '

    # Debug
    print('Debug Secret Number: ' + str(secret_number))
    # Debug
    while secret_number:
        attempt_txt = ' - Attempts: ' + str(attempt) + '/5 '
        if attempt > max_try:
            print('You lose - Game Over')
            break
        guess = int(input(guess_txt))

        if secret_number == guess:
            print('Congratulation ' + attempt_txt)
            break
        elif secret_number > guess:
            print('Sorry Wrong Guess - Your guess was too small ' + attempt_txt)
        elif secret_number < guess:
            print('Sorry Wrong Guess - Your guess was too high ' + attempt_txt)

        attempt = attempt + 1

