def matroshka (n):
    if n==1:
        print("matroshechka")
    else:
        print("vverh matreshki n=", n)
        matroshka (n-1)
        print("niz matroshki n=", n)


#matroshka(int(input()))


def f (n:int):
    assert n>=0
    if n==0:
        return 1
    return f(n-1)*n


def gcd (a,b):
    if a==b:
        return a
    elif a>b:
        return gcb(a-b,b)
    else:
        return gcd (a,b-a)
