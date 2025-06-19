import numpy as np
import matplotlib.pyplot as plt

def linear(x, k, b): return k*x+b
def quad(x, a, b, c): return a*x**2+b*x+c
def sin(x, a, b): return a*np.sin(b*x)
def exp(x, a, b): return a*np.exp(b*x)
def log(x, a, b): return a*np.log(np.abs(b*x))

print("Задайте границы графика через запятую:")
xmin, xmax = map(float, input("Xmin, Xmax = ").split(","))
ymin, ymax = map(float, input("Ymin, Ymax = ").split(","))

x = np.linspace(xmin, xmax, 10000)

print("\nДоступные функции:")
print("1) Линейная: y = k*x + b")
print("2) Квадратичная: y = a*x^2 + b*x + c")
print("3) Синус: y = a*sin(b*x)")
print("4) Экспонента: y = a*exp(b*x)")
print("5) Логарифм: y = a*log(b*x)")

def select():
    choice = int(input("Выберите функцию (1-5): "))
    
    if choice == 1:
        k, b = map(float, input("k, b = ").split(","))
        y = linear(x, k, b)
        n = f"Линейная (k={k}, b={b})"
    elif choice == 2:
        a, b, c = map(float, input("a, b, c = ").split(","))
        y = quad(x, a, b, c)
        n = f"Квадратичная (a={a}, b={b}, c={c})"
    elif choice == 3:
        a, b = map(float, input("a, b = ").split(","))
        y = sin(x, a, b)
        n = f"Синус (a={a}, b={b})"
    elif choice == 4:
        a, b = map(float, input("a, b = ").split(","))
        y = exp(x, a, b)
        n = f"Экспонента (a={a}, b={b})"
    elif choice == 5:
        a, b = map(float, input("a, b = ").split(","))
        y = log(x, a, b)
        n = f"Логарифм (a={a}, b={b})"
    else:
        print("Неверный номер!")
        return None, None
    
    return y, n

print("\nПервая функция:")
y1, n1 = select()
if y1 is None: exit()

print("\nВторая функция:")
y2, n2 = select()
if y2 is None: exit()

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=n1)
plt.plot(x, y2, label=n2)

title = f"Сравнение: {n1} и {n2}"

cross = []
diff = y1 - y2
exact_cross = np.where(np.abs(diff) < 1e-10)[0]
for i in exact_cross:
    cross.append((x[i], y1[i]))

for i in range(len(x) - 1):
    if diff[i] * diff[i+1] < 0:
        x_cross = x[i] - diff[i] * (x[i+1] - x[i]) / (diff[i+1] - diff[i])
        y_cross = y1[i] + (y1[i+1] - y1[i]) * (x_cross - x[i]) / (x[i+1] - x[i])
        cross.append((x_cross, y_cross))

cross = list(set((round(x, 8), round(y, 8)) for x, y in cross))

if cross:
    for x_val, y_val in cross:
        plt.plot(x_val, y_val, 'ro', markersize=5)
    
    print(f"\nНайдены точки пересечения ({len(cross)} шт.):")
    title += f"\nНайдены точки пересечения ({len(cross)} шт.):"
    for i, (x_val, y_val) in enumerate(cross):
        print(f"{i+1}: x={x_val:.4f}, y={y_val:.4f}")
        title += f"\n{i+1}: x={x_val:.4f}, y={y_val:.4f}"
else:
    print("Точки пересечения не найдены")
    title += "\nТочки пересечения не найдены"

plt.title(title, fontsize=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis([xmin, xmax, ymin, ymax])
plt.show()