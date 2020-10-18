class car():
    """класс по созданию авто"""
    def __init__ (self, make, model, year):
        """инациализация атрибутов авто"""
        self.make=make
        self.model=model
        self.year=year
        self.odemetr_reding = 0#атрибут со значением ноль

    def description_name(self):
        """возвращаем описания переменной"""
        desc=str(self.year)+' '+self.make+' '+self.model
        return desc.title()

    def probeg (self):
        """выводим пробег авто"""
        print("пробег этого авто "+ str(self.odemetr_reding)+ ":km/h")

    def meniat_km(self, km):
        """устанавливаем значения одометр"""
        if km>=self.odemetr_reding:
            self.odemetr_reding=km
        else:
            print("ай крыса пробег хочешь скрутить")

    def uvelich(self, km):
        """увеличиваем значения одометра на заданную переменную"""
        if km>0:
            self.odemetr_reding += km
        else:
            print("так нельзя минусовую")

"""---------------------------------"""
class batari ():

    def __init__ (self, battery=100):
        self.battery=battery

    def descripshon_battery(self):
        """выводит инфу про мощности батареи"""
        print("этот авто имеет батарею "+str(self.battery))
"""============================="""

class electrik_car(car):#указываем откуда мы наследуем класс/ класс которыйс строится на основном родителе на классе кар а потом отец класса электроникс кар
    """аспекты для электромобили"""
    def __init__ (self, make, model, year):#делаем одинаково с кар
        super().__init__ (make, model, year)  #функция super помогает связать несколько классов вместе наследственных классов
        self.battery=batari()##связываем с отдельным классом

    def description_name(self):
        """если мы загоняем так переменную новую то он читает уже ее то есть последнюю а не ту которая в модительском """
        desc=str(self.year)+" "+self.model
        return desc.title()

print('Dias')

