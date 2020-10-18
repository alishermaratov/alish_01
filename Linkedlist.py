class Box:

    """СОЗДАНИЯ СПИСКА"""
    def __init__ (self,cat = None):#СПИСОК ПОКА ПУСТОЙ ИЗА ЭТОГО НОНЕ
        self.cat = cat
        self.nextcat = None

class LinkedList:
    def __init__(self):
            self.head = None#НАЧАЛО СПИСКА


"""Содержится ли элемент в списке"""

    def contains (self, cat):
        lastbox = self.head#ПРИСВАЕВАЕМ ПЕРЕМЕННУЮ К СОЗДАННОМУ СПИСКУ
        while (lastbox):#ЦИКЛ БУДЕТ ПРОДОЛЖАТСЯ ДО ТОГО ПОКА НЕ ЗАКОНЧАТСЯ ЦИФРЫ
            if cat == lastbox.cat:#ЕСТЬ ЛИ ЭТОТ ЭЛЕМЕНТ В СПИСКЕ
                return True#ТО ВЫВОДИМ ТРУ
            else:
                lastbox = lastbox.nextcat
                return False

"""Добавить узел в конец списка"""

     def addToEnd(self, newcat):
         newbox = Box(newcat)#ТУТ ВЫЗЫВАЕМ КЛАСС БОКС СО ЗНАЧЕНИЯМ НОВЫМ
         if self.head is None:#ЕСЛИ СПИСОК ПУСТОЙ ТО
             self.head = newbox#ЗАМЕНЯЕМ ЭТИМ ЗНАЧЕНИЯМ
             return
         lastbox = self.head
         while (lastbox.nextcat):
             lastbox = lastbox.nextcat
         lastbox.nextcat = newbox

"""Получить узел по индексу"""

     def get(self, catIndex):
         lastbox = self.head
         boxIndex = 0
         while boxIndex <= catIndex:
             if boxIndex == catIndex:
                 return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat


"""Удалить узел"""
     def removeBox(self,rmcat):
         headcat = self.head

         if headcat is not None:
             if headcat.cat==rmcat:
                 self.head = headcat.nextcat
                 headcat = None
                 return
         while headcat is not None:
             if headcat.cat==rmcat:
                 break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat == None:
            return
        lastcat.nextcat = headcat.nextcat
        headcat = None
