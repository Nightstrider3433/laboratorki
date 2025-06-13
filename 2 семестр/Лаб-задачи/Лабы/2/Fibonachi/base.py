def fibSequence(n):
    """Генерация последовательности Фибоначчи с n числами, используя итерационный подход"""
    assert n > 0
    series = [1]
    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    return series

def fibRecurse(n):
    """Рекурсивная генерация послесовательности Фибоначчи с n числами"""
    if n <= 2:
        return 1
    return fibRecurse(n-1) + fibRecurse(n-2)

def getFibSequence(n):
    """Получение последовательности Фибоначчи из n чисел, используя рекурсивную функцию."""
    return [fibRecurse(i+1) for i in range(n)]

if __name__ == "__main__":
    n = int(input('Сколько чисел? '))
    print(f"Итерационный метод: {fibSequence(n)}")
    print(f"Рекурсивный метод: {getFibSequence(n)}")