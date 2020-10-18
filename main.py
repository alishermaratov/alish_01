# import moduli#импортируем файл который мы писали до этого всее коды идут туда
print(locals())
print()

from moduli import token#*это импорт всех обьявленных пременных

print(token)
print(dir(moduli))#смотрю есть ли и добавился ли переменная токен
print(moduli.token)#выводит переменную токен мне
print(locals())
