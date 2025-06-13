def isPrime(x):
    """Проверка на простое число."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def genPrime(currentPrime):
    """Генерация следующего простого числа."""
    newPrime = currentPrime + 1
    while True:
        if not isPrime(newPrime):
            newPrime += 1
        else:
            break
    return newPrime

def findNearestPrime(x):
    """Нахождение ближайшего простого числа."""
    if x < 2:
        return 2
        
    if isPrime(x):
        return x
    
    lower = x - 1
    higher = x + 1
    
    while True:
        if isPrime(lower):
            return lower
        elif isPrime(higher):
            return higher
        lower -= 1
        higher += 1

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите число для проверки на простоту (или 'q' для выхода): ")
            
            if user_input.lower() == 'q':
                break
                
            number = int(user_input)
            
            if isPrime(number):
                print(f"Число {number} является простым.")
            else:
                print(f"Число {number} не является простым.")
                nearest_prime = findNearestPrime(number)
                print(f"Ближайшее простое число: {nearest_prime}")
                
        except ValueError:
            print("Пожалуйста, введите целое число.")