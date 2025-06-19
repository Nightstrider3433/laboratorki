import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QDesktopWidget, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
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
        btn_calculator.clicked.connect(self.show_calculator)
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
    
    def show_calculator(self):
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
        btn_calculator.clicked.connect(self.show_calculator_info)

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
    
    def show_calculator_info(self):
        self.calculator_form = CalculatorForm()
        self.calculator_form.show()

class CalculatorForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
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

app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())