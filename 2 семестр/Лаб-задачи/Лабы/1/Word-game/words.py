import random

list_of_words = [ 
    'яблоко',  'победа',  'программирование', 'терминал',  'ноутбук' 
] 
random_word = list_of_words[random.randint(0, len(list_of_words) - 1)] 
set_of_symbols = set(random_word) 
discovered_symbols = set()
available_letters   = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
used_by_bot = set()
player_health = 2
bot_health = 20
print('_ ' * len(random_word)) 
turn = 0

while True:

    if turn == 0:
        print("\nВаш ход:")
        
        if discovered_symbols != set_of_symbols and player_health > 0:
            disc_symbol = input('> ')
            assert len(disc_symbol) == 1
            if player_health == 0: 
                print('Жизни закончились :(') 
                break
            if disc_symbol in discovered_symbols:
                print('Вы уже вводили эту букву, попробуйте что-нибудь другое')
                turn = 1

            elif disc_symbol not in set_of_symbols:
                player_health -= 1
                print(f'Этой буквы нет в слове. Текущее кол-во жизней: {player_health}')
                turn = 1
            else:
                print('Буква есть в слове!')
                discovered_symbols.add(disc_symbol)
                turn = 1
            current_word_progress = ''
            for ch in random_word:
                current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
            print(current_word_progress)
            turn = 1
    
    if turn == 1:
        print("\nХод компьютера:")
        
        if discovered_symbols != set_of_symbols and bot_health > 0:
            
            if available_letters:
                disc_symbol = random.choice(list(available_letters))
                used_by_bot.add(disc_symbol)

            if bot_health == 0: 
                print('Жизни закончились :(') 
                break
            if disc_symbol in set_of_symbols:
                print(f"Компьютер попробовал букву '{disc_symbol}' и угадал!")
                discovered_symbols.add(disc_symbol)
                turn = 0
            else:
                bot_health -= 1
                print(f"Компьютер ошибся! Оставшиеся попытки: {bot_health}")
                turn = 0
            current_word_progress = ''
            for ch in random_word:
                current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
            print(current_word_progress)
            turn = 0
    if bot_health <= 0:
        print("Бот проиграл, вы выйграли!")
        break
    if player_health <= 0:
        print("Вы проиграли, бот выйграл!")
        break
    if discovered_symbols == set_of_symbols:
        print(f"Загаданное слово было {random_word} \nИгра окончена")
        break




import random 

list_of_words = [ 
'яблоко',  'победа',  'программирование', 'терминал',  'ноутбук' 
] 
random_word = list_of_words[random.randint(0, len(list_of_words) - 1)] 
set_of_symbols = set(random_word) 
discovered_symbols = set() 
health = 5 
print('_ '*len(random_word)) 
while discovered_symbols != set_of_symbols and health > 0: 
    user_symbol = input('> ') 
    assert len(user_symbol) == 1 

    if user_symbol in discovered_symbols: 
        print('Вы уже вводили эту букву, попробуйте что-нибудь другое') 
    elif user_symbol not in set_of_symbols: 
        health -= 1 
        print('Этой буквы нет в слове. Текущее кол-во жизней: {}'.format(health)) 
    elif user_symbol in set_of_symbols: 
        print('Буква есть в слове!') 
    discovered_symbols.add(user_symbol) 
    current_word_progress = '' 
    for ch in random_word: 
        current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' ' 
    print(current_word_progress) 
if health == 0: 
    print('Жизни закончились :(') 
else: 
    print('Поздравляю, вы правильно набрали слово {}'.format(random_word))