import time
import os
import random
import sys

CHAR_LIFE= "* " # Символ живой клетки
CHAR_EMPTY= ". "# Символ пустой/мертвой клетки
CONST_GENERATION = 5000 # количество поколений в игре
CONST_TIME_SLEEP = 1 / 5.0 # время задержки вывода поля игры по умолчанию 1/5 секунды

ERR_CLS_OS_Unsupported= "Невозможно очистить терминал. Ваша операционная система не поддерживается.\n\r"
ERR_RESIZE_OS_Unsupported= "Невозможно изменить размер терминала. Ваша операционная система не поддерживается.\n\r"
ERR_NOT_Integer= "Введено недопустимое целое значение."
ERR_Integer_not_in_range= "Введенное число должно быть в диапазоне от {0} до {1}."
STR_INFO= "Поколение {0} - для выхода из программы нажмите <Ctrl-C>\n\r"
STR_Input_rows= "Введите количество строк в игре (10-60): "
STR_Input_cols= "Введите количество столбцов в игре (10-118): "
STR_PRESS_Enter_TO_EXIT= "Нажмите <Enter> для завершения или r для новой игры: "

def clear_console():
###
# Очищает консоль с помощью системной команды в зависимости от операционной системы пользователя.
###
    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")
    else:
        print(ERR_CLS_OS_Unsupported)

def resize_console(rows, cols):
###
# Изменяет размер консоли до размера rows x cols.
# :param rows: Int — количество строк для изменения размера консоли.
# :param cols: Int — количество столбцов для изменения размера консоли.
###
    if cols < 32:
        cols = 32

    if sys.platform.startswith('win'):
        command = "mode con: cols={0} lines={1}".format(cols + cols, rows + 5)
        os.system(command)
    elif sys.platform.startswith('linux'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    elif sys.platform.startswith('darwin'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    else:
        print(ERR_RESIZE_OS_Unsupported)

def create_initial_grid(rows, cols):
###
# Создает случайный список списков (двумерный список/массив), содержащий 1 и 0, представляющий ячейки в игре «Жизнь» Конвея.
# :param rows: Int — количество строк в сетке Game of Life.
# :param cols: Int — количество столбцов в сетке Game of Life.
# :return: Int[][] — список списков, содержащий 1 для живых и 0 для мертвых
# ячеек.
###
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
        # Сгенерируем случайное число и на его основе решим, добавлять ли в сетку живую или мертвую ячейку.
            if random.randint(0, 7) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid

def print_grid(rows, cols, grid, generation):
###
# Распечатывает на консоли поле игры.
# :rows: Int — количество строк в поле.
# :cols: Int — количество столбцов в поле.
# :grid: Int[][] — Список списков, который используется для представления поля
# :generation: Int — Номер текущего поколения поля
###
    clear_console()
    # Одна строка вывода используется для уменьшения мерцания, вызванного печатью нескольких строк.
    output_str = ""
    # Соберем выходную строку и затем распечатайте ее на консоли.
    output_str += STR_INFO.format(generation)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += CHAR_EMPTY
            else:
                output_str += CHAR_LIFE
        output_str += "\n\r"
    print(output_str, end=" ")

def create_next_grid(rows, cols, grid, next_grid):
###
# Анализирует текущее поколение на поле Игры и определяет, какие клетки живут и умирают в следующем.
# :rows: Int — количество строк в поле игры
# :cols: Int — количество столбцов в поле игры
# :grid: Int[][] — Список списков, который будет использоваться для
# представления поля Игры текущего поколения.
# :next_grid: Int[][] — Список списков, который будет использоваться для представления поля Игры следующего поколения.
###
    for row in range(rows):
        for col in range(cols):
        # Получим количество живых ячеек, соседних с ячейкой grid[row][col]
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)
            # Если количество окружающих живых ячеек < 2 или > 3, мы делаем мертвой ячейку grid[row][col]
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            # Если количество окружающих живых ячеек равно 3, а ячейка grid[row][col] ранее была мертвой,
            # то делаем ее живой
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            # Если количество окружающих живых ячеек равно 3, а ячейка grid[row][col] жива, то сохраняем ее живой.
            else:
                next_grid[row][col] = grid[row][col]

def get_live_neighbors(row, col, rows, cols, grid):
###
# Подсчитывает количество живых ячеек, окружающих ячейку grid[row][cell].
# :param row: Int — строка клетки.
# :param col: Int — столбец клетки.
# :param rows: Int — количество строк в поле Игры.
# :param cols: Int — количество столбцов в поле Игры.
# :param grid: Int[][] — Список списков, который использеутся для представления поля Игры.
# :return: Int — итговый результат: количество живых ячеек, окружающих ячейку grid[row][cell]
###
    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Обязательно посчитайте центральную ячейку, расположенную в grid[row][cell]
            if not (i == 0 and j == 0):
                #Используем оператор остатка от деления (%)
                life_sum += grid[((row + i) % rows)][((col + j) % cols)]
    return life_sum

def grid_changing(rows, cols, grid, next_grid):
###
# Проверяет, совпадает ли текущее поле игры с полем следующего поколения.
# :param rows: Int — количество строк в игре.
# :param cols: Int — количество столбцов в игре .
# :paramgrid: Int[][] — Список списков, который используется для представления поля игры текущего поколения.
# :param next_grid: Int[][] — Список списков, который будет использоваться для представления поля следующего поколения Игры.
# :return: Логическое значение — совпадает ли сетка текущего поколения с сеткой следующего поколения.
###
    for row in range(rows):
        for col in range(cols):
            # Если ячейка grid[row][col] не равна next_grid[row][col]
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False

def get_integer_value(prompt, low, high):
###
# Запрашивает у пользователя целочисленный ввод между заданными границами нижнего и верхнего пределов.
# :param prompt: String — строка, запрашивающая у пользователя о вводе
# :param low: Int — нижняя граница, в пределах которой пользователь должен оставаться.
#:param high: Int — верхняя граница, в пределах которой должен оставаться пользователь.
# :return: Допустимое входное значение, введенное пользователем.
###
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(ERR_NOT_Integer)
            continue
        if value < low or value > high:
            print(ERR_Integer_not_in_range.format(low, high))
        else:
            break
    return value

def create_own_grid(rows, cols):
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            grid_rows += [0]
        grid += [grid_rows]

    for j in range(rows):
        print(f"{j}: ", end="") # Выводим номер строки без перехода на новую строку
        str_input = input() # Считываем строку ввода
        
        for i in range(min(cols, len(str_input))):
            if str_input[i] == '*':
                grid[j][i] = 1 # Если есть звездочка в строке, заносим в поле 1
            else: # иначе заносим 0
                grid[j][i] = 0
    return grid

def run_game():
###
# Запрашивает у пользователя исходные данные для настройки игры «Жизнь» для запуска заданного количества поколений.
###
    clear_console()
    # Вводим количество строк и столбцов в поле игры.
    rows = get_integer_value(STR_Input_rows, 10, 60)
    clear_console()
    cols = get_integer_value(STR_Input_cols, 10, 118)
    clear_console()
    resize_console(rows, cols)
    # Создаем начальное поле игры
    #current_generation = create_initial_grid(rows, cols)
    print("Введите начальное поколение ('*' - живая клетка, ' ' - мертвая клетка):")
    current_generation = create_own_grid(rows, cols)
    next_generation = create_initial_grid(rows, cols)
    # Основной цикл игры
    gen = 1
    for gen in range(1, CONST_GENERATION + 1):
        if not grid_changing(rows, cols, current_generation, next_generation):
            break
        print_grid(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(CONST_TIME_SLEEP)
        current_generation, next_generation = next_generation, current_generation
    print_grid(rows, cols, current_generation, gen)
    return input(STR_PRESS_Enter_TO_EXIT)

# Основная программа - запускает в цикле функцию run_game()
run = "r"
while run == "r":
    out = run_game()
    run = out