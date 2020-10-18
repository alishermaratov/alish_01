a = 5
b = 6

c = 1
d = 2

max = 32


def sum_int(a:int, b:int):
    print(a + b)


def get_dias():
    max = 'Dias'
    return max


def plus_alish(s):
    return s + ' Alish'


bar = get_dias()
alish = plus_alish(bar)
print(alish)


iinbin = '000719550573'


def checker_iinbin(iinbin):
    foo = iinbin[4]
    if int(foo) <= 3:
        return True
    else:
        return False


checker_iinbin(iinbin)


if checker_iinbin(iinbin):
    print('iin')
else:
    print('bin')



def max(A):
    b = 0
    for a in A:
        if a > b:
            b = a
    print('chetam')
    return b


A = [1, 2, 3, 4, 99, 5, 6, 7, 8, 9, 45]

for i in A:
    print(i)

max_int = max(A)

print(max_int)
