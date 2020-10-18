#---------------------генерация всех перестановок------------------------
def generate_number(N:int, M:int, prefix=None):
    prefix=prefix or []
    print(prefix)#проверка работает ли у меня функция (выводит [])



# ДЛЯ ПРОИЗВОЛЬНОЙ ТАК КАК МОЖНО УКАЗЫВАТЬ СИСТЕМЫ СЧАСТЛЕНИЯ И СКОЛЬКО БУДЕТ РАЗ ГЕНЕРИРОВАТЬ
def generate_numbers(N:int, M:int, prefix=None):#начало функции строим сами prefix это просто пустой список так как префикс ноне ноль
#n основания системы счастления и М это количество чисел prefi
#--------------------------генирирует все числа с лидирующями нулями
    prefix = prefix or []#если prefix равено none то он ложный. none это ложь
    if M == 0:
        print(prefix)
        return
    for digit in range (N):
        prefix.append(digit)#цыфры форика фигачим в прификс а прификс у нас пустой массив туда все собираем диджит это повторения форика как видишь
        generate_numbers(N, M-1, prefix)
        prefix.pop()#.pop удаляет элемент в этом случае последний

#--------------------------ГЕНЕРАТОВ ЦИФР ТОЛЬКО ДЛЯ ДВОИЧНОЙ СИСТЕМЫ СЧАСТЛЕНИЯ
def gen_bin (M, prefix=""):#ТОЛЬКО ДЛЯ ДВОИЧНОЙ СИСТЕМЫ СЧАСТЛЕНИЯ
    if M == 0:
        print(prefix)
    else:
        gen_bin (M-1, prefix+"0")
        gen_bin (M-1, prefix+"1")

# ---------------------------------------перестановка всех чисел в генераторе чисел

def find (number, A):# ищет number в А и возвращает тру если такой есть фолс
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
        return flag



def generate_permutations(N:int, M:int=-1, prefix=None):
    M=M if M != -1 else N
    prefix = prefix or []
    if M==0:
        print(prefix)
        return
    for number in range (1, N+1):
        if find (number, prefix):#функция которая ищет число
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(2)



# ----------------------------------рекурентное сортировка------------------
# в следуйщей реализация
# 1)тони хуара быстрое сортировка //// выполняется на прямом ходу рекрсии
#    не нужна доп памяти
# разделяй и властвуй
#
#
# 2)слияния сортировка ///// а здесь на обратном ходу когда возвращаемся
#     но нужна дополнительная память
# 
