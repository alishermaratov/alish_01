massiv = [
    [1, 2, 35, 3],
    [4, 5, 18, 6],
    [7, 8, 9, 6]
]

max = 0
for lift in massiv:
    for row in lift:
        if max < row:
            max = row
#print(max)

max = 0

for i in range(3):
    for j in range(4):
        if max < massiv[i][j]:
            max = massiv[i][j]

print(max)
