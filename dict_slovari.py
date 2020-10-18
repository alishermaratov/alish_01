"""словари dictionary"""
a=['astana','almaty','uralsk']


"""первый способ создать словарь"""
d={
'astana': 7272,
'almaty': 8888,#это словарь и словарь это присваевания значения через множества элементу массива
'uralsk': 5656
}#значения могут быть любых типов и ключи могут быть типов инт и строка
print(d)

"""второй способ с функцией dict"""
r= dict(astana=555, almaty=599, urarlsk=589595) #ФУНКЦИЯ ДИК АВТОМАТИЧЕСКИЙ ПРИСВАЕВАЕТ ЗНАЧЕНИЯ И ПЕРЕВОДИТ ВСЕ В ТЕКСТ
#----------такой способ используется только тогда когда у меня значения именно строковые типы
print(r)


"""третий способ создания словаря"""
a=[['astana',445],['almaty',895],['uralsk',7845]]
t=dict(a)
print(t)

"""четвертый способ создания словаря"""
q=dict.fromkeys(['a','b','c'],1105)#если я ничего не уажу то уже
print(q)

"""пустой словарь"""
v={ }#первый способ
print(v,type(v))
c=dict()#второй способ
print(c,type(c))

"""обращения внутри массива"""
d={
'astana': 7272,
'almaty': 8888,#astana i almaty это ключи а рядом это значения ключа
 2: 'two'
}
d[4]='four'#добавления еще ключа
print(d['astana'])#если только одно значения
print(d[2])
print(4)



person={}
s="iwefnsdjinvd infjdjkvnd sijkndvjkfnv sdevdvedv 5 4 32 5 3 5"
s=s.split()#разделить по пробелам и запятым
person['a1']=s[0]
person['a2']=s[1]
person['a3']=s[2]
person['a4']=s[3]
person['a5']=[]
for i in s[4:]:
    person['a5'].append(int(i))#добавили значения

print(s)
print(person)

"""удалить один элемент со словаря"""
d={
 1: "effe",
 2: "ffef",#astana i almaty это ключи а рядом это значения ключа
 3: 'two'
}
print(d)
del d[1]#удалил элемент под ключем 1
print(d)

""" функции словаря"""
d={
 1: "effe",
 2: "ffef",#astana i almaty это ключи а рядом это значения ключа
 3: 'two'
 }
print(d)
print(len(d))#сколько имеется пар ключ
print(1 in d, 2 in d, 5 in d)#есть ли этот ключ в словаре
print(d.get(1))#если этот ключ есть то он выводит нам это значения
print(d.get(8,50)) #ЕСЛИ ЭТОГО КЛЮЧА НЕТ ТО МОЖНО ПРИСВОИТЬ ТАМ ЖЕ ЗНАЧЕНИЯ КАК ТУТ ПРИСВАОИЛИ 50
d.setdefault(7,550)#если значения нет то добовяет ключ со значениям none через запятую можно будет передать значения элементу
print(d.pop(1))#dвыведет мне значения этого ключа но при этом в дальнейшем удалит это значения
print(d)
print(d.keys())#значения всех ключей

"""
Методы в словарей

dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.


Когда нужно использовать словари
Словари нужно использовать в следующих случаях:

1)Подсчет числа каких-то объектов. В этом случае нужно завести словарь, в котором ключами являются объекты, а значениями — их количество.
2)Хранение каких-либо данных, связанных с объектом. Ключи — объекты, значения — связанные с ними данные. Например, если нужно по названию месяца определить его порядковый номер, то это можно сделать при помощи словаря Num['January'] = 1; Num['February'] = 2; ....
3)Установка соответствия между объектами (например, “родитель—потомок”). Ключ — объект, значение — соответствующий ему объект.
4)Если нужен обычный массив, но при этом масимальное значение индекса элемента очень велико, но при этом будут использоваться не все возможные индексы (так называемый “разреженный массив”), то можно использовать ассоциативный массив для экономии памяти.
"""