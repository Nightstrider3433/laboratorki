from random import *

# Выбор режима

validchoice = False
while not validchoice:
    choice = input("Выберите режим игры (1 - игрок vs бот (3x3), 2 - игрок vs игрок (5x5)): ")
    try:
        choice = int(choice)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        continue
    if choice == 1:
        print("*" * 10, " Игра Крестики-нолики для игрок против бота (3x3) ", "*" * 10)
        board = list(range(1, 10))
        validchoice = True
    elif choice == 2:
        print("*" * 10, " Игра Крестики-нолики для двух игроков (5x5)", "*" * 10)
        board = list(range(1, 26))
        validchoice = True
    else:
        print("Некорректный ввод. Вы уверены, что ввели верное число?")

# Рисование доски

def draw_board(board):
    if choice == 1:
        print("-" * 13)
        for i in range(3):
            for x in range(3):
                print("|", board[x + i * 3], "", end="")
            print("|")
            print("-" * 13)
    elif choice == 2:
        print("-" * 26)
        for i in range(5):
            for x in range(5):
                if ((x + i * 5) + 1) < 10:
                    print("|", board[x + i * 5], " ", end="")
                else:
                    numb = True
                    try:
                        board[x + i * 5] = int(board[x + i * 5])
                    except:
                        numb = False
                    if numb == True:
                        print("|", board[x + i * 5], "", end="")
                    else:
                        print("|", board[x + i * 5], " ", end="")
            print("|")
            print("-" * 26)

# Ход игрока

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if choice == 1:
            if 1 <= player_answer <= 9:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
        else:
            if 1 <= player_answer <= 25:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 25.")

# Ход бота

def bot_input(player_token):
    valid = False
    while not valid:
        if choice == 1:
            player_answer = randint(1, 9)
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
        else:
            player_answer = randint(1, 25)
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
    print("Бот ходит на", player_answer, "клетку!")

# Проверка выигрыша

def check_win(board):
    if choice == 1:
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False
    else:
        win_coord = ((0, 1, 2), (1, 2, 3), (2, 3, 4), (5, 6, 7), (6, 7, 8), (7, 8, 9), (10, 11, 12),
                     (11, 12, 13), (12, 13, 14), (15, 16, 17), (16, 17, 18), (17, 18, 19), (20, 21, 22),
                     (21, 22, 23), (22, 23, 24), (0, 5, 10), (5, 10, 15), (10, 15, 20), (1, 6, 11),
                     (6, 11, 16), (11, 16, 21), (2, 7, 12), (7, 12, 17), (12, 17, 22), (3, 8, 13),
                     (8, 13, 18), (13, 18, 23), (4, 9, 14), (9, 14, 19), (14, 19, 24), (0, 6, 12),
                     (6, 12, 18), (12, 18, 24), (1, 7, 13), (7, 13, 19), (2, 8, 14), (5, 11, 17),
                     (11, 17, 23), (10, 16, 22), (4, 8, 12), (8, 12, 16), (12, 16, 20), (3, 7, 11),
                     (7, 11, 15), (2, 6, 10), (9, 13, 17), (13, 17, 21), (14, 18, 22))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

# Игра

def main(board):
    counter = 0
    win = False
    bot_var = False
    while not win:
        draw_board(board)
        if choice == 1:
            if not bot_var:
                bot = randint(0, 1)
                bot_var = True
                if bot == 0:
                    print("Первым ходит бот!")
                else:
                    print("Первым ходите вы!")
            if bot == 0:
                if counter % 2 == 0:
                    bot_input("X")
                else:
                    take_input("O")
            else:
                if counter % 2 == 0:
                    take_input("X")
                else:
                    bot_input("O")
        else:
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if choice == 1:
            if counter == 9:
                print("Ничья!")
                break
        else:
            if counter == 25:
                print("Ничья!")
                break
    draw_board(board)

main(board)
input("Нажмите Enter для выхода!")