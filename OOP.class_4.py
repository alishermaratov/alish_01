#"""импорт классов будем доставать модули с прошлого урока """
from class_car import car
"""иморт класса сюда происходит так фром (откуда) и импорт самого класса который нужен"""

BMW=car("BMW", "x7", 2020)
print(BMW.description_name())
BMW.probeg()


import class_car#первый способ импортировать все
"""если я хочу обращаться все модули брать то я должен буду каждый раз писать имя файла а потом только что хочу сделать"""

BMW=class_car.car("BMW", "x7", 2020)
print(BMW.description_name())
BMW.probeg()


from class_car import*
"""это импотирования все че есть в этом файле и в этом случае не нужно писать каждый раз имя файла через точку"""

BMW=car("BMW", "x7", 2020)
print(BMW.description_name())
BMW.probeg()
