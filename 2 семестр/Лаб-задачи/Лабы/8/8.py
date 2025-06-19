import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QVBoxLayout, QLabel, QDesktopWidget, QPushButton, QLineEdit, QColorDialog, QFontDialog, QFileDialog, QTextEdit, QToolBar, QMessageBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt

global global_color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('&Файл')
        
        new_action = QAction(QIcon(), 'Новый', self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction(QIcon(), 'Открыть', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction(QIcon(), 'Сохранить', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction(QIcon(), 'Выход', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        labs_menu = menubar.addMenu('&Лабораторные работы')

        lab1_action = QAction('Лаб 1.3: Генератор паролей', self)
        lab1_action.triggered.connect(self.show_password)
        labs_menu.addAction(lab1_action)

        lab2_action = QAction('Лаб 2.1: Рекурсивный алгоритм чисел Фибоначчи', self)
        lab2_action.triggered.connect(self.show_recurse)
        labs_menu.addAction(lab2_action)

        lab3_action = QAction('Лаб 6: Графики', self)
        lab3_action.triggered.connect(self.show_plot)
        labs_menu.addAction(lab3_action)
        
        lab4_action = QAction('Лаб 7: Квест и калькулятор', self)
        lab4_action.triggered.connect(self.show_quest)
        labs_menu.addAction(lab4_action)
        
        settings_menu = menubar.addMenu('&Настройки')
        
        color_action = QAction('Цвет фона', self)
        color_action.triggered.connect(self.change_background)
        settings_menu.addAction(color_action)
        
        font_action = QAction('Шрифт', self)
        font_action.triggered.connect(self.change_font)
        settings_menu.addAction(font_action)
        
        help_menu = menubar.addMenu('&Справка')
        
        about_action = QAction('О программе', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        toolbar = QToolBar('Основные инструменты')
        self.addToolBar(toolbar)
        
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addSeparator()
        toolbar.addAction(about_action)
        
        self.statusBar().showMessage('Готово')
        
        self.text_edit = QTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        central_widget.setLayout(layout)
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Универсальное приложение PyQt')
        self.show()
    
    def new_file(self):
        self.text_edit.clear()
        self.statusBar().showMessage('Создан новый файл')
    
    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)')
        if fname:
            with open(fname, 'r') as f:
                self.text_edit.setText(f.read())
            self.statusBar().showMessage(f'Файл {fname} загружен')
    
    def save_file(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)')
        if fname:
            with open(fname, 'w') as f:
                f.write(self.text_edit.toPlainText())
            self.statusBar().showMessage(f'Файл {fname} сохранён')
    
    def change_background(self):
        global global_color
        color = QColorDialog.getColor()
        if color.isValid():
            global_color = color
            self.setStyleSheet(f"background-color: {color.name()};")
            self.statusBar().showMessage(f'Цвет фона изменён на {color.name()}')
    
    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)
            self.statusBar().showMessage(f'Шрифт изменён на {font.family()}')

    def show_recurse(self):    
        self.recurse = RecurseForm()
        self.recurse.show()

    def show_password(self):    
        self.password = PasswordForm()
        self.password.show()

    def show_quest(self):
        self.calculator = QuestForm()
        self.calculator.show()
    
    def show_plot(self):
        self.plot = PlotForm()
        self.plot.show()
    
    def show_about(self):
        QMessageBox.information(self, 'О программе', 'Универсальное приложение PyQt\n' 'Включает 4 лабораторные работы\n' 'и демонстрацию диалоговых окон')

# ------ Рекурс. числа --------------

class RecurseForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 225, 150)
        self.center()
        self.setWindowTitle('Рекурсивный алгоритм чисел Фибоначчи')

        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Сколько чисел?"))
        self.number_edit = QLineEdit()
        self.number_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.number_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()

    def save_params(self):
        n = self.number_edit.text()
        if n == "":
            n = 0
        else:
            n = int(n)
        fib = ', '.join(str(x) for x in self.fibRecurse(n))
        QMessageBox.information(self, 'Успех!', f'Ваши числа Фибоначчи: {fib}')
        self.close()
    
    def fibRecurse(self, n):
        assert n > 0
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        
        series = self.fibRecurse(n-1)
        series.append(series[-1] + series[-2])
        return(series)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# ------ Генератор паролей ----------

class PasswordForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Генератор паролей')

        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Введите адрес сайта:"))
        self.site_edit = QLineEdit()
        self.site_edit.setPlaceholderText("Введите адрес сайта")
        vbox.addWidget(self.site_edit)

        vbox.addWidget(QLabel("Введите логин:"))
        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Введите логин")
        vbox.addWidget(self.login_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        site = self.site_edit.text()
        if site == 'q':
            self.close()
        login = self.login_edit.text()
        if login == 'q':
            self.close()
        password = []
        for i in range(random.randint(2, 4)):
            password.append(chr(random.randint(65, 90))) # uppercase
        for i in range(random.randint(2, 4)):
            password.append(chr(random.randint(97, 122))) #lowercase
        for i in range(random.randint(2, 4)):
            password.append(chr(random.randint(48, 57))) # digits
        for i in range(random.randint(2, 4)):
            password.append(chr(random.randint(33, 148))) # special
        random.shuffle(password)
        passw = ''.join(password)
        with open('passwords.txt', 'w') as file:
            file.write(site + '\n')
            file.write(login + '\n')
            file.write(passw[:len(passw)] + '\n')
        QMessageBox.information(self, 'Успех!', f'Сгенерированный пароль: {passw}' '\nСохранено в файл passwords.txt')
        self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# ------------ Графики --------------

global xplot, xmin, xmax, ymin, ymax, y1, n1, y2, n2, g1

class PlotForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")
            
        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Границы Графика')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Задайте границы графика:"))

        vbox.addWidget(QLabel("Xmin:"))
        self.xmin_edit = QLineEdit()
        self.xmin_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.xmin_edit)

        vbox.addWidget(QLabel("Xmax:"))
        self.xmax_edit = QLineEdit()
        self.xmax_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.xmax_edit)

        vbox.addWidget(QLabel("Ymin:"))
        self.ymin_edit = QLineEdit()
        self.ymin_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.ymin_edit)

        vbox.addWidget(QLabel("Ymax:"))
        self.ymax_edit = QLineEdit()
        self.ymax_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.ymax_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, xmin, xmax, ymin, ymax, g1
        xmin = self.xmin_edit.text()
        if xmin == "":
            xmin = 0
        else:
            xmin = float(xmin)
        xmax = self.xmax_edit.text()
        if xmax == "":
            xmax = 0
        else:
            xmax = float(xmax)

        ymin = self.ymin_edit.text()
        if ymin == "":
            ymin = 0
        else:
            ymin = float(ymin)
        ymax = self.ymax_edit.text()
        if ymax == "":
            ymax = 0
        else:
            ymax = float(ymax)

        xplot = np.linspace(xmin, xmax, 10000)

        g1 = False

        self.ploty = PlotYForm()
        self.ploty.show()
        self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def linear(xplot, k, b): return k*xplot+b
def quad(xplot, a, b, c): return a*xplot**2+b*xplot+c
def sin(xplot, a, b): return a*np.sin(b*xplot)
def exp(xplot, a, b): return a*np.exp(b*xplot)
def log(xplot, a, b): return a*np.log(np.abs(b*xplot))

class LinearForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Линейная функция')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Линейная функция:"))

        vbox.addWidget(QLabel("k:"))
        self.k_edit = QLineEdit()
        self.k_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.k_edit)

        vbox.addWidget(QLabel("b:"))
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.b_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, y1, n1, g1, y2, n2
        k = float(self.k_edit.text())
        b = float(self.b_edit.text())
        if not g1:
            y1 = linear(xplot, k, b)
            n1 = f"Линейная (k={k}, b={b})"

            g1 = True

            self.ploty = PlotYForm()
            self.ploty.show()
            self.close()
        else:
            y2 = linear(xplot, k, b)
            n2 = f"Линейная (k={k}, b={b})"

            do_plt()
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class QuadForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 275, 150)
        self.center()
        self.setWindowTitle('Квадратичная функция')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Квадратичная функция:"))

        vbox.addWidget(QLabel("a:"))
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.a_edit)

        vbox.addWidget(QLabel("b:"))
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.b_edit)

        vbox.addWidget(QLabel("c:"))
        self.c_edit = QLineEdit()
        self.c_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.c_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, y1, n1, g1, y2, n2
        a = float(self.a_edit.text())
        b = float(self.b_edit.text())
        c = float(self.c_edit.text())
        if not g1:
            y1 = quad(xplot, a, b, c)
            n1 = f"Квадратичная (a={a}, b={b}, c={c})"

            g1 = True

            self.ploty = PlotYForm()
            self.ploty.show()
            self.close()
        else:
            y2 = quad(xplot, a, b, c)
            n2 = f"Квадратичная (a={a}, b={b}, c={c})"

            do_plt()
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class SinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")
            
        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Синус функция')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Синус функция:"))

        vbox.addWidget(QLabel("a:"))
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.a_edit)

        vbox.addWidget(QLabel("b:"))
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.b_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, y1, n1, g1, y2, n2
        a = float(self.a_edit.text())
        b = float(self.b_edit.text())
        if not g1:
            y1 = sin(xplot, a, b)
            n1 = f"Синус (a={a}, b={b})"

            g1 = True

            self.ploty = PlotYForm()
            self.ploty.show()
            self.close()
        else:
            y2 = sin(xplot, a, b)
            n2 = f"Синус (a={a}, b={b})"

            do_plt()
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class ExpForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")
            
        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Экспонента функция')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Экспонента функция:"))

        vbox.addWidget(QLabel("a:"))
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.a_edit)

        vbox.addWidget(QLabel("b:"))
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.b_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, y1, n1, g1, y2, n2
        a = float(self.a_edit.text())
        b = float(self.b_edit.text())
        if not g1:
            y1 = exp(xplot, a, b)
            n1 = f"Экспонента (a={a}, b={b})"

            g1 = True

            self.ploty = PlotYForm()
            self.ploty.show()
            self.close()
        else:
            y2 = exp(xplot, a, b)
            n2 = f"Экспонента (a={a}, b={b})"

            do_plt()
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class LogForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Логарифм функция')

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Логарифм функция:"))

        vbox.addWidget(QLabel("a:"))
        self.a_edit = QLineEdit()
        self.a_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.a_edit)

        vbox.addWidget(QLabel("b:"))
        self.b_edit = QLineEdit()
        self.b_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.b_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        global xplot, y1, n1, g1, y2, n2
        a = float(self.a_edit.text())
        b = float(self.b_edit.text())
        if not g1:
            y1 = log(xplot, a, b)
            n1 = f"Логарифм (a={a}, b={b})"

            g1 = True

            self.ploty = PlotYForm()
            self.ploty.show()
            self.close()
        else:
            y2 = log(xplot, a, b)
            n2 = f"Логарифм (a={a}, b={b})"

            do_plt()
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class PlotYForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        global g1
        self.setGeometry(300, 300, 200, 150)
        self.center()
        if not g1:
            self.setWindowTitle('Первая функция')
        else:
            self.setWindowTitle('Вторая функция')

        vbox = QVBoxLayout()
        if not g1:
            vbox.addWidget(QLabel("Выберите первую функцию:\n1) Линейная: y = k*xplot + b\n2) Квадратичная: y = a*xplot^2 + b*xplot + c\n3) Синус: y = a*sin(b*xplot)\n4) Экспонента: y = a*exp(b*xplot)\n5) Логарифм: y = a*log(b*xplot)"))
        else:
            vbox.addWidget(QLabel("Выберите вторую функцию:\n1) Линейная: y = k*xplot + b\n2) Квадратичная: y = a*xplot^2 + b*xplot + c\n3) Синус: y = a*sin(b*xplot)\n4) Экспонента: y = a*exp(b*xplot)\n5) Логарифм: y = a*log(b*xplot)"))

        self.func_edit = QLineEdit()
        self.func_edit.setPlaceholderText("Введите число")
        vbox.addWidget(self.func_edit)

        self.btn_save = QPushButton("Далее")
        self.btn_save.clicked.connect(self.save_params)
        vbox.addWidget(self.btn_save)

        self.setLayout(vbox)
        self.show()
    
    def save_params(self):
        func = int(self.func_edit.text())
        if func == 1:
            self.linearform = LinearForm()
            self.linearform.show()
            self.close()
        elif func == 2:
            self.quadform = QuadForm()
            self.quadform.show()
            self.close()
        elif func == 3:
            self.sinform = SinForm()
            self.sinform.show()
            self.close()
        elif func == 4:
            self.expform = ExpForm()
            self.expform.show()
            self.close()
        elif func == 5:
            self.logform = LogForm()
            self.logform.show()
            self.close()
        else:
            self.close()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def do_plt():
    plt.figure(figsize=(10, 6))
    plt.plot(xplot, y1, label=n1)
    plt.plot(xplot, y2, label=n2)

    title = f"Сравнение: {n1} и {n2}"

    cross = []
    diff = y1 - y2
    exact_cross = np.where(np.abs(diff) < 1e-10)[0]
    for i in exact_cross:
        cross.append((xplot[i], y1[i]))

    for i in range(len(xplot) - 1):
        if diff[i] * diff[i+1] < 0:
            x_cross = xplot[i] - diff[i] * (xplot[i+1] - xplot[i]) / (diff[i+1] - diff[i])
            y_cross = y1[i] + (y1[i+1] - y1[i]) * (x_cross - xplot[i]) / (xplot[i+1] - xplot[i])
            cross.append((x_cross, y_cross))

    cross = list(set((round(xplot, 8), round(y, 8)) for xplot, y in cross))

    if cross:
        for x_val, y_val in cross:
            plt.plot(x_val, y_val, 'ro', markersize=5)
        
        title += f"\nНайдены точки пересечения ({len(cross)} шт.):"
        for i, (x_val, y_val) in enumerate(cross):
            title += f"\n{i+1}: xplot={x_val:.4f}, y={y_val:.4f}"
    else:
        title += "\nТочки пересечения не найдены"

    plt.title(title, fontsize=10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()

# ------------ Квест ----------------

class QuestForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(300, 300, 500, 400)
        self.center()
        self.setWindowTitle('Рабочий стол программиста')
        
        btn_electronics = QPushButton('Электроника', self)
        btn_accessories = QPushButton('Аксессуары', self)
        btn_calculator = QPushButton('Калькулятор', self)
        btn_quest = QPushButton('Начать квест', self)
        btn_about = QPushButton('О программе', self)
        
        btn_electronics.clicked.connect(self.show_electronics)
        btn_accessories.clicked.connect(self.show_accessories)
        btn_calculator.clicked.connect(self.show_quest)
        btn_quest.clicked.connect(self.start_quest)
        btn_about.clicked.connect(self.show_about)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Что вы хотите осмотреть?"))
        vbox.addWidget(btn_electronics)
        vbox.addWidget(btn_accessories)
        vbox.addWidget(btn_calculator)
        vbox.addStretch()
        vbox.addWidget(btn_quest)
        vbox.addWidget(btn_about)
        
        self.setLayout(vbox)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def show_electronics(self):
        self.form1 = ElectronicsForm()
        self.form1.show()
    
    def show_accessories(self):
        self.form2 = AccessoriesForm()
        self.form2.show()
    
    def show_quest(self):
        self.form3 = CalculatorForm()
        self.form3.show()
    
    def show_about(self):
        QMessageBox.information(self, 'О программе', 'Показывает описание предметов на рабочем столе.\n' 'Включает калькулятор и интерактивный квест.')
    
    def start_quest(self):
        reply = QMessageBox.question(self, 'Начало квеста', 'Вы программист и у вас важный дедлайн! ' 'Вы готовы начать работу?', QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.show_electronics()
        else:
            QMessageBox.critical(self, 'Провал', 'Вы не успели к дедлайну! Проект провален.')
            self.close()


class ElectronicsForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(350, 350, 300, 250)
        self.setWindowTitle('Электроника')
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите электронное устройство:"))
        
        btn_keyboard = QPushButton('Клавиатура', self)
        btn_mouse = QPushButton('Мышь', self)
        btn_monitor = QPushButton('Монитор', self)
        btn_laptop = QPushButton('Ноутбук', self)
        
        btn_keyboard.clicked.connect(self.show_keyboard_info)
        btn_mouse.clicked.connect(self.show_mouse_info)
        btn_monitor.clicked.connect(self.show_monitor_info)
        btn_laptop.clicked.connect(self.show_laptop_info)
        
        layout.addWidget(btn_keyboard)
        layout.addWidget(btn_mouse)
        layout.addWidget(btn_monitor)
        layout.addWidget(btn_laptop)
        
        btn_back = QPushButton('Назад', self)
        btn_back.clicked.connect(self.close)
        layout.addWidget(btn_back)
        
        self.setLayout(layout)
    
    def show_keyboard_info(self):
        QMessageBox.information(self, 'Клавиатура', 'Основное устройство ввода.\n' 'Механическая, RGB-подсветка, 104 клавиши.\n' 'Используется для набора кода и текста.')
    
    def show_mouse_info(self):
        QMessageBox.information(self, 'Мышь', 'Устройство для управления курсором.\n' 'Оптическая, беспроводная, 5 кнопок.\n' 'DPI: 1600')
    
    def show_monitor_info(self):
        QMessageBox.warning(self, 'Монитор', 'Основное устройство вывода.\n' '27 дюймов, 4K разрешение, 144Hz.\n' '⚠️ Не смотрите слишком близко к экрану!')
    
    def show_laptop_info(self):
        reply = QMessageBox.question(self, 'Ноутбук', 'Мощный игровой ноутбук.\n' 'Хотите запустить среду разработки?', QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.accessories_form = AccessoriesForm()
            self.accessories_form.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Без кода не получится выполнить задание!')


class AccessoriesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")

        self.setGeometry(350, 350, 300, 250)
        self.setWindowTitle('Аксессуары')
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите аксессуар:"))
        
        btn_mug = QPushButton('Кружка', self)
        btn_headphones = QPushButton('Наушники', self)
        btn_notebook = QPushButton('Блокнот', self)
        btn_calculator = QPushButton('Калькулятор', self)

        btn_mug.clicked.connect(self.show_mug_info)
        btn_headphones.clicked.connect(self.show_headphones_info)
        btn_notebook.clicked.connect(self.show_notebook_info)
        btn_calculator.clicked.connect(self.show_quest_info)

        layout.addWidget(btn_mug)
        layout.addWidget(btn_headphones)
        layout.addWidget(btn_notebook)
        layout.addWidget(btn_calculator)
        
        btn_back = QPushButton('Назад', self)
        btn_back.clicked.connect(self.close)
        layout.addWidget(btn_back)
        
        self.setLayout(layout)
    
    def show_mug_info(self):
        QMessageBox.critical(self, 'Внимание!', 'Горячая кружка с кофе!\n''☕️ Не проливайте на клавиатуру!')
    
    def show_headphones_info(self):
        reply = QMessageBox.question(self, 'Наушники', 'Беспроводные наушники с шумоподавлением.\n' 'Надеть их для лучшей концентрации?', QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Успех!', 'Вы прекрасно сконцентрировались!\n' '✅ Код написан, дедлайн выполнен!')
        else:
            QMessageBox.warning(self, 'Проблема', 'Вас отвлекли коллеги.\n' '⏰ Вы не успели к дедлайну!')
    
    def show_notebook_info(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Блокнот для заметок")
        msg.setInformativeText("Что вы хотите сделать?")
        msg.setWindowTitle("Блокнот")
        msg.setDetailedText("Доступные действия:\n- Нарисовать схему\n- Записать идею\n- Составить план")
        msg.setStandardButtons(QMessageBox.Save | QMessageBox.Ignore | QMessageBox.Cancel)
        ret = msg.exec_()
        
        if ret == QMessageBox.Save:
            QMessageBox.information(self, 'Сохранено', 'Идея записана!')
        elif ret == QMessageBox.Ignore:
            QMessageBox.warning(self, 'Упущено', 'Хорошая идея забыта...')
    
    def show_quest_info(self):
        self.calculator_form = CalculatorForm()
        self.calculator_form.show()

class CalculatorForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        global global_color
        if global_color:
            self.setStyleSheet(f"background-color: {global_color.name()};")
            
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle('Калькулятор')
        
        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        font = self.display.font()
        font.setPointSize(24)
        self.display.setFont(font)

        buttons = [
            '7', '8', '9', 'C', '⌫',
            '4', '5', '6', '*', '/',
            '1', '2', '3', '+', '-',
            '0', '.', '='
        ]
        
        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 5)
        
        positions = [(i, j) for i in range(1, 5) for j in range(5)]
        
        for position, button in zip(positions, buttons):
            btn = QPushButton(button)
            btn.setFixedSize(50, 50)
            btn.clicked.connect(self.button_click)
            grid.addWidget(btn, *position)
        

        btn_back = QPushButton('Назад', self)
        btn_back.clicked.connect(self.close)
        grid.addWidget(btn_back, 5, 0, 1, 5)
        
        self.setLayout(grid)
        self.current = ''
    
    def button_click(self):
        action = self.sender().text()
        
        if action == 'C':
            self.current = ''
        elif action == '⌫':
            self.current = self.current[:-1]
        elif action == '=':
            try:
                self.current = str(eval(self.current))
            except Exception:
                self.current = 'Error'
        else:
            self.current += action
            
        self.display.setText(self.current)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())