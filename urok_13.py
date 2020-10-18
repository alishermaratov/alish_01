#
"""steck
модуль описавающий структуру данных -стек
push(1)#вход в очередь
push(2)
push(3)
is_empty()
False
pop()#выход оттуда
3
pop()
2
pop()
1
is_empty()
True
"""
_stack=[]

def push(x):
    _stack.append(x)

def pop():
    x=_stack.pop()
    return x

def clear ():
    _stack.clear()

def is_empty():
    return True #len(_stack)==0

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
