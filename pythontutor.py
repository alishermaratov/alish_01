A = [ 78, 6, 7, 4, 88, 9, 9, 11, 115]

b=0
m=0
for index in range(1, len(A)):
    if A[index] > b:
        b = A[index]
    if A[index] < m:
        m = A[index]
A[b],A[m] = A[m],A[b]
print(' '.join([str(index) for index in A]))
# print(m)
# print(z)
# print(s)
# print(b)





#print(i)
#print(A[i])
