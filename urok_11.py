# двумерные масссивы динамическое прогромировния продолжения
"""наиблольшая общая подпоследовательность"""
#а и б это массивы len(a)==n, len(b)==m
#подпоследовательность ---- с который мсодержит элементы а в исходном порядке. но возможно не все
def lcs(a,b):
    f=[ [0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range (1,len(a)+1):
        for j in range (1,len(b)+1):
            if a[i-1]==b[j-1]:
                f[i][j]=1+f[i-1][j-1]
            else:
                f[i][j]=max([i-1][j],f[i][j-1])
        return f[-1][-1]
# c=lcs(2,2)
# print(c)



"""наиблольшая возвращаемая  подпоследовательность"""
def gis(a):
    f=[0]*(len(a)+1)
    for i in range (1,len(a)+1):
        m=0
        for i in range(0, i):
            if a[i]>a[j] and f[j]>m:
                m=f[j]
        f[i]=m+1
    return F[len(a)]

# c=gis(2)
# print(c)
