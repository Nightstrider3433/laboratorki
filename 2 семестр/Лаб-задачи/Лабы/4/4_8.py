class Bird:
    def fly(self):
        pass

    def sing(self):
        pass

class Eagle(Bird):
    def fly(self):
        return "Орел летит высоко"
    
    def sing(self):
        return "Крик орла"

class Parrot(Bird):
    def fly(self):
        return "Попугай летит на уровне домов"
    
    def sing(self):
        return "Песня попугая"

class Penguin(Bird):
    def fly(self):
        return "Пингвин не умеет летать"
    
    def sing(self):
        return "Крик пингвина"    

eagle = Eagle()
print(eagle.fly())
print(eagle.sing())

parrot = Parrot()
print(parrot.fly())
print(parrot.sing())

penguin = Penguin()
print(penguin.fly())
print(penguin.sing())