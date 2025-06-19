class Transportation:
    def start_engine(self):
        pass
    
    def stop_engine(self):
        pass

class Car(Transportation):
    def start_engine(self):
        print("Запуск двигателя автомобиля")
    
    def stop_engine(self):
        print("Остановка двигателя автомобиля")

class Motorcycle(Transportation):
    def start_engine(self):
        print("Запуск двигателя мотоцикла")
    
    def stop_engine(self):
        print("Остановка двигателя мотоцикла")

class Train(Transportation):
    def start_engine(self):
        print("Запуск двигателя поезда")
    
    def stop_engine(self):
        print("Остановка двигателя поезда")

car = Car()
car.start_engine()
car.stop_engine()

motorcycle = Motorcycle()
motorcycle.start_engine()
motorcycle.stop_engine()

train = Train()
train.start_engine()
train.stop_engine()