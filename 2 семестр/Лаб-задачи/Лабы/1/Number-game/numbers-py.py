import random

random_number = random.randint(1, 100)

print('Компьютер и человек по очереди пытаются угадать число от 1 до 100.')

user_guess = 0
computer_guess = 0
low, high = 1, 100
turn = 'user'  # очередность

while user_guess != random_number and computer_guess != random_number:
    if turn == 'user':
        user_guess = int(input('Ваш ход. Введите число: '))
        if user_guess > random_number:
            print('Меньше!')
        elif user_guess < random_number:
            print('Больше!')
        else:
            print('Вы угадали!')
        turn = 'computer'
    else:
        computer_guess = random.randint(low, high)
        print(f'Ход компьютера: {computer_guess}')
        if computer_guess > random_number:
            print('Меньше!')
            high = computer_guess - 1
        elif computer_guess < random_number:
            print('Больше!')
            low = computer_guess + 1
        else:
            print('Компьютер угадал!')
        turn = 'user'
