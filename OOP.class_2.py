#
"""классы и экзенпляры"""

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



my_car = car('audi','a4',2007)

print(my_car.description_name())
#my_car.odemetr_reding = 30#можно прямо отсюда регулировать __init__
my_car.meniat_km(30)#мы вызвали метод они все работают слаженно


my_car.uvelich(25)#добавляем км
my_car.probeg()
