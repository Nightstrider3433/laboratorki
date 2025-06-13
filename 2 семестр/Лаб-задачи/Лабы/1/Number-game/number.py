import random

n, m = 1, 1000
random_number = random.randint(n, m)
user_guess = 0
computer_guess = 0
LowInput, HighInput = n, m
turn = '1'  # очередность, 1 - игрок, 2 - компьютер

print(f'Игра "Угадай число" - задаётся случайное число от {n} до {m}.\nИгрок и компьютер, угадывают число каждый ход.\nКто первый угадал - тот и выиграл.\nНачало игры! ')

while user_guess != random_number and computer_guess != random_number:
    if turn == '1':
        user_guess = int(input('Ваш ход. Введите число: '))
        if user_guess > random_number:
            print('Загаданное число меньше.')
            if user_guess > LowInput and user_guess < HighInput:
                HighInput = user_guess - 1
        elif user_guess < random_number:
            print('Загаданное число больше.')
            if user_guess < HighInput and user_guess > LowInput:
                LowInput = user_guess + 1
        else:
            print('Вы угадали!')
        print(f'Загаданное число где-то от {LowInput} до {HighInput}')
        turn = '2'
    else:
        computer_guess = random.randint(LowInput, HighInput)
        print(f'Ход компьютера: {computer_guess}')
        if computer_guess > random_number:
            print('Загаданное число меньше.')
            HighInput = computer_guess - 1
        elif computer_guess < random_number:
            print('Загаданное число больше.')
            LowInput = computer_guess + 1
        else:
            print('Компьютер угадал!')
        print(f'Загаданное число где-то от {LowInput} до {HighInput}')
        turn = '1'
