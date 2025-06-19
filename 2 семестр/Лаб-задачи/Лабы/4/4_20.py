class ElectronicDevice:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    def charge(self):
        pass

class Smartphone(ElectronicDevice):
    def take_photo(self):
        print("Сделан снимок на смартфон")
    
    def make_call(self):
        print("Звонок через смартфон")

class Laptop(ElectronicDevice):
    def search_www(self):
        print("Был выполнен поиск страницы через ноутбук")
    
    def email_boss(self):
        print("Сообщение боссу на эл. почту через ноутбук")

class Tablet(ElectronicDevice):
    def play_games(self):
        print("Была запущена игра на планшете")
    
    def watch_film(self):
        print("Просмотр кино через планшет")

smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()

laptop = Laptop()
laptop.search_www()
laptop.email_boss()

tablet = Tablet()
tablet.play_games()
tablet.watch_film()