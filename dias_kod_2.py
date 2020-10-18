
                 # """бинарный поиск маассива , binary_search"""
A = [1,12,45,65,86,91,92,100,111]
start = 0
stop = len(A)
key = 45
a = 55


def binary_search(A:list, key:int, start:int, stop:int):
    if start > stop:
        return False
    middle = (start+stop)//2
    if key == A[middle]:
        return middle
    elif key < A[middle]:
         return binary_search(A, key, start, middle-1)
    else:
        return binary_search(A, key, middle+1, stop)


# s = binary_search(A, a, start, stop)
#
#
# print(s)

""" нахождения слова в предоставленном списке"""

def counter(s:str):#функция со строковым значением
    count = 0
    k = 0
    d = s.lower()#lower это делает все буквы мальенками, если хоть одна буква заглавленная то ее делает мальенкой
    while k<len(s):
        if d[k] in 'alks':#тут ищет сколько букв есть на всем списке буквы которые совподают с ин
            count+=1 #если цикл успешен и он находит то плюсует один в count
        k+=1#дальше плюсует на один чтобы цикл продолжался и цикл будет продолжатся до тех пор пока к  не бкдет равен длине слова
    return count

c=counter("Assalamualeykum")

print(c)
