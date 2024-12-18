from random import randint

user = 0
computer = 0

def guess_number():
    return randint(1,100)

computer_think = randint(1,100)

while True:
    try:
        user_think = int(input('Number : '))
    except:
        print('Enter only integer numbers')
        continue
    print(computer_think)

    if user_think > computer_think:
        computer += 1
        print('Too high!')

    elif user_think < computer_think:
        computer += 1
        print('Too low!')
    else:
        print('You guessed it right!')
        break

    if computer == 10:
        again = input('You lost. Want to play again? ')
        if again in ['Y', 'YES', 'y', 'yes', 'ok']:
            user = 0
            computer = 0
            computer_think = guess_number()
            continue
        else:
            break
