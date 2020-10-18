""" ООП КЛАССЫ"""

class Dog():#создаем класс


    def __init__(self , name, age):#даем значения сразу
        self.name = name #привязываем значения имя на селф имя
        self.age = age #
        #print("собака создана")

    def sit(self): #простая команда, функция которая вызывает когда нужно
        print(self.name.title() + " собака села")#self нужен для того чтобы они связывались и общались между собой

    def jump(self):
        print(self.name.title() + " собака прыгнула ")

    def gav(self):
        print(self.name.title() + " гав гав собака гавкнула ")


my_dog = Dog("Mirkuri", 5)#вот так присваеваем переменной значения
my_dog_2=Dog("aliii", 9)
print(my_dog.name)
print(my_dog.age)#так можно вызывать имя

my_dog.jump()#обращаемся к переменной которую присвоели и вызываем функцию (пишем что хотел бы сделать собака)
my_dog.sit()
my_dog.gav()

print("")

my_dog_2.jump()
my_dog_2.sit()
my_dog_2.gav()
