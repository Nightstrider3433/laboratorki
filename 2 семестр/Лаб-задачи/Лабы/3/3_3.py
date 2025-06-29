import os
import random
import time
from threading import Thread

import datetime

if os.getenv("OS") in ["Windows_NT", "Linux"]:
    import msvcrt as m

player_name = ""

# Начальные значения
x = 5
y = 3
game_thread = True
fruit_cord_x = 5
fruit_cord_y = 6
button_default = "d"
score = 0
icon_player = "►"
tail = "o"
last2X, last2Y, lastX, lastY = 0, 0, 0, 0
elemX = [0] * 100
elemY = elemX.copy()

def clear():
    if os.getenv("OS") == "Windows_NT":
        os.system("cls")
    elif os.getenv("OS") in [None, "Linux"]:
        os.system("clear")

def game_over():
    global player_name, game_thread
    with open('result.txt', 'w') as file:
        file.write(player_name + '\n')
        file.write(str(datetime.datetime.now()) + '\n')
        file.write(str(score) + '\n')
    print("\nGAME OVER\nВаши очки: {0}. Ваш результат был записан в файл 'result.txt'.".format(score))
    game_thread = False
    exit()

def board(width: int = 40, height: int = 20, pos_player_x: int = x, pos_player_y: int = y):
    global score, fruit_cord_x, fruit_cord_y, game_thread, icon_player, last2X, lastX, lastY, last2Y, elemY, elemX
    clear()
    for i in range(height):
        for j in range(width):
            if pos_player_x == fruit_cord_x and pos_player_y == fruit_cord_y:
                fruit_cord_x = random.randint(5, width - 1)
                fruit_cord_y = random.randint(5, height - 1)
                score += 1

            for el in range(score):
                if pos_player_x == elemX[el] and pos_player_y == elemY[el]:
                    game_over()

            if not (x in range(width - 39)) and not (y in range(height - 1)) or not (x in range(width - 1)) and not ( y in range(height - 19)):
                game_over()

            if j == 0:
                print("\t", end="")
                print('#', end='')
            elif i == 0:
                print('#', end='')
            elif i == height - 1:
                print('#', end='')
            elif j == width - 1:
                print('#', end='')
            elif pos_player_x == j and pos_player_y == i:
                print(icon_player, end='')
            elif fruit_cord_x == j and fruit_cord_y == i:
                print("*", end='')
            else:
                pr = True
                for ls in range(score):
                    if elemX[ls] == j and elemY[ls] == i:
                        print(tail, end="")
                        pr = False
                if pr:
                    print(' ', end='')

        print()
    # интерфейс
    print(f"\tОчки: {score}\n\n\t\tWASD / Стрелочки - перемещение\n\t\t\tESC - выйти")
    lastX, lastY = pos_player_x, pos_player_y
    if score > 0:
        for el in range(score):
            last2X, last2Y = elemX[el], elemY[el]
            elemX[el], elemY[el] = lastX, lastY
            lastX, lastY = last2X, last2Y

def button_move():
    global button_default
    if os.getenv("OS") in ["Windows_NT", "Linux"]:
        while game_thread:
            button_default = m.getch()[0]
    else:
        while game_thread:
            button_default = input("Нажмите кнопку перемещения: ")

def move():
    global x, y, game_thread, button_default, icon_player

    while game_thread:
        if button_default in ["", " "]:
            button_default = "d"
        elif button_default in ["w", 119, 230, 72]:
            y -= 1
            icon_player = "▲"
        elif button_default in ["a", 97, 228, 75]:
            x -= 1
            icon_player = "◄"
        elif button_default in ["s", 115, 235, 80]:
            y += 1
            icon_player = "▼"
        elif button_default in ["d", 100, 162, 77]:
            x += 1
            icon_player = "►"

        elif button_default in ["exit", 27]:
            print("Вы покинули игру\nВаши очки: {0} - выши очки не были засчитаны".format(score))
            game_thread = False
            exit()

        board(pos_player_x=x, pos_player_y=y)

        time.sleep(.2)

def main():
    board()
    Thread(target=move).start()
    Thread(target=button_move).start()

def menu():
    global player_name
    clear()
    print("Программа консольная змейка | Управление - стрелки клавиатуры\n\n\t\t1 - Играть\n\t\t2 - Посмотреть результаты\n\t\t3 - Выход")
    if os.getenv("OS") in ["Windows_NT", "Linux"]:
        btn = m.getch()[0]
    else:
        btn = input("Выберите пункт: ")
    if btn in ["1", 49]:
        clear()
        player_name = input("Введите ваше имя: ")
        main()
    elif btn in ["2", 50]:
        clear()
        print("Ваши предыдущие результаты: ")
        if os.path.exists("result.txt"):
            lines = []
            with open('result.txt') as file:
                lines = [line.rstrip() for line in file]
            print("Имя: " + lines[0])
            print("Дата и время: " + lines[1])
            print("Результат: " + lines[2])
        else:
            print("У вас еще нет записанных результатов!")
        input()
    elif btn in ["3", 51]:
        exit()

menu()