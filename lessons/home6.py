class Hero:
    def __init__(self, power=0, durability=0, luck=0, magic=0):
        self.__power = power
        self.__durability = durability
        self.__luck = luck
        self.__magic = magic

    def setpwr(self, power):
        self.__power = power

    def getpwr(self):
        return self.__power

    def setdrbly(self, durability):
        self.__durability = durability

    def getdrbly(self):
        return self.__durability

    def setlck(self, luck):
        self.__luck = luck

    def getlck(self):
        return self.__luck

    def setmgc(self, magic):
        self.__magic = magic

    def getmgc(self):
        return self.__magic


hr = Hero()
hr.setpwr(33)
hr.setdrbly(55)
hr.setlck(55)
hr.setmgc(22)
print(f'Сила-{hr.getpwr()}, Оборона-{hr.getdrbly()}, Удача-{hr.getlck()}, Магия-{hr.getmgc()}')