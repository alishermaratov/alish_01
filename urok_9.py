# ----------------------------------рекурентное сортировка------------------
# в следуйщей реализация
# 1)тони хуара быстрое сортировка //// выполняется на прямом ходу рекрсии
#    не нужна доп памяти
# разделяй и властвуй
#
#
# 2)слияния сортировка ///// а здесь на обратном ходу когда возвращаемся
#     но нужна дополнительная память

"""---------------------сортировка слияния-------------------"""
# слияния отсортированных масииовов
def merge(a:list, b:list): #цель а массив и б массив на входе а на выходе большой с массив
    c=[0]*(len(a)+len(b))
    i=0
    k=0
    n=0#------------------сортировка называетсмя устойчевой, если она не меняет порядок равных элементов
    while i<len(a) and k<len(b): #индекс не должен выходить с границ своего массива
        if a[i]<=b[k]:#если нулевой или какойто элемент ниже и массива то он идет в пустой массив с
            c[n]=a[i]
            i+=1 #чтоб цикл дальше шел и не стоял на месте
            n+=1 #тоже чтоб цикл шел
        else:
            c[n]=b[k]
            k+=1
            n+=1
    while i<len(a):#если один из списков закончится надо же его пустить в масиив с вот и создан
        c[n]=a[i]#пока i не больше чем лен цикл будет идти и он будет продолжатся когда цикл закончится то значит и массив закончился
        i+=1
        n+=1
    while k < len(b):
        c[n]=b[k]
        k+=1
        n+=1
    return c


"""===================рекурсивная функция"""
def merge_sort(a):
    if len(a)<=1:
        return
    middle=len(a)//2
    l=[a[i] for i in range (0, middle)]
    r=[a[i] for i in range (middle, len(a))]
    merge_sort(l)
    merge_sort(r)
    c=merge(l,r)
    for i in range (len(a)):#скапировать с массива с на массив а
        a[i]=c[i]

"""====================================сортировка слияния это"""
j=[4,5,6,4,8,1,5]
merge_sort(j)
print(*j)


"""# ========================================сортировка тони хоара//////быстрая сортировка"""
def hoar_sort(a):
    if len(a)<=1:
        return #none это нечего прямо нечего даже не ноль
    barier=a[0]
    l=[]
    m=[]
    r=[]
    for x in a:
        if x<barier:
            l.append(x)
        elif x== barier:
            m.append(x)
        else:
            r.append(x)
    hoar_sort(l)
    hoar_sort(r)
    k=0
    for x in l + m + r:
        a[k]=x
        k+=1


hoar_sort(j)
print(j)


def chek_sorted(a,ascending=True):
    """проверка отсортированности за o(len(a))"""
    flag=True
    s= 2*int(ascending)-1
    for i in range(0, n-1):
        if s*a[i] > s*a[i+1]:
            flag=False
            break
        return flag

            """бинарный поиск в массиве"""
