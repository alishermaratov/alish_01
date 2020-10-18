def insert_sort(A):
    """сортировка списка A вставками
    Объяснение
Предполагается, что первый элемент списка отсортирован.
 Затем мы переходим к следующему элементу, назовем его х.
 Если x больше первого элемента, мы оставляем его как
 есть. Если x меньше, мы копируем значение первого
 элемента во вторую позицию и затем устанавливаем первый
 элемент в x.

Когда мы переходим к другим элементам
несортированного сегмента, мы непрерывно перемещаем
более крупные элементы в отсортированном сегменте вверх
 по списку, пока не встретим элемент меньше x, или не
  достигнем конца отсортированного сегмента, а затем
  поместим x в его правильное положение."""
    N=len(A)
    for top in range(1, N):
        k=top
        while k > 0 and A[k-1] > A[k]:
            A [k] , A[k-1] = A[k-1], A[k]
            k -= 1



def choise_sort(A):
    """сортировка списка А выбором"""
    N=len(A)
    for pos in range(0, N-1):
        for k in range(pos+1,N):
            if A[k]<A[pos]:
                A[k], A[pos]=A[pos], A[k]


def bubble_sort(A):
    """ сортировка списка A методом пузырька
    Пузырьковая сортировка (Bubble Sort)
Этот самый простой алгоритм сортировки который выполняет
итерации по списку, сравнивая элементы попарно
и меняя их местами, пока более крупные элементы не
перестанут «всплывать» до конца списка,
а более мелкие элементы не будут оставаться «снизу»."""
    N=len(A)
    for bypase in range (1, N):
        for k in range (0, N-bypass):
            if A[k]>A[k+1]:
                A[k], A[k+1]=A[k+1], A[k]







def test_sort(sort_alorithm):
    print("testcase1:", end="")
    A=[4, 2, 5, 1, 3]
    A_sorted=[1, 2, 3, 4, 5]
    sort_alorithm(A)
    print("ok"if A==A_sorted else "fail")


    print("testcase2:", end="")
    A= list(range(10,20))+list(range(0,10))
    A_sorted=list (range(20))
    sort_alorithm(A)
    print("ok"if A==A_sorted else "fail")


    print("testcase3:", end="")
    A=[4, 2, 5, 1, 5]
    A_sorted=[1, 2, 2, 1, 4]
    sort_alorithm(A)
    print("ok"if A==A_sorted else "fail")

#if  name == " main ":
    # test_sort(insert_sort)
    # test_sort(choise_sort)
    # test_sort(bubble_sort)
# A=[6,8,2,81,6,1,3,8,1,2,3]
# a=test_sort(A)
#
# #a=insert_sort(A)
# print(a)
