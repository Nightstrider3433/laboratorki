import math

def calc(a, b, op):
    if op not in '+-/*%^s':
        return 'Пожалуйста, выберите тип операции: "+, -, *, /, %, ^, s"!'
    
    if op == '+':
        return f'{a} {op} {b} = {a + b}'
    
    if op == '-':
        return f'{a} {op} {b} = {a - b}'
    
    if op == '*':
        return f'{a} {op} {b} = {a * b}'
    
    if op == '/':
        if b == 0:
            return 'Деление на ноль запрещено!'
        return f'{a} {op} {b} = {a / b}'
    
    if op == '%':
        return f'{b}% от {a} = {(a * b) / 100}'
    
    if op == '^':
        return f'{a}^{b} = {pow(a, b)}'
    
    if op == 's':
        if a < 0 or b < 0:
            return 'Квадратный корень из отрицательного числа невозможен!'
        return f'√{a} = {math.sqrt(a)} и √{b} = {math.sqrt(b)}'

def main():
    while True:
        try:
            print("\nВведите два числа:")
            a = float(input('Пожалуйста, введите первое число: '))
            b = float(input('Пожалуйста, введите второе число: '))
            
            print("\nВыберите операцию:")
            print("  + : Сложение")
            print("  - : Вычитание")
            print("  * : Умножение")
            print("  / : Деление")
            print("  % : Вычисление процента")
            print("  ^ : Возведение в степень")
            print("  s : Извлечение квадратного корня из обоих чисел")
            
            op = input('\nКакой вид операции Вы желаете осуществить? ')
            
            result = calc(a, b, op)
            print(result)
            
            another = input('\nХотите выполнить еще одну операцию? (y/n): ')
            if another.lower() != 'y':
                break
                
        except ValueError:
            print('Ошибка: Пожалуйста, вводите только числовые значения!')
        except Exception as e:
            print(f'Произошла ошибка: {e}')
 
if __name__ == '__main__':
    main()