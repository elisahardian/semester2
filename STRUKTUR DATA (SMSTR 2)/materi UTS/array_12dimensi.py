## ARRAY 1 DIMENSI
array = []
array.append(1)
array[0]=12
print(array)
print()

## ARRAY 2 DIMENSI
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)
print(m[0])
print(m[1])
print(m[2])
print(m[0][0], m[0][1], m[0][2])
print(m[1][0], m[1][1], m[1][2])
print(m[2][0], m[2][1], m[2][2])
print()
for i in m:
    print(i)
print()
for i in m:
    for j in i:
        print(j)
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(m[i][j], end=" ")
    print()
print()
matriks = []
matriks.append([1, 0, 0])
matriks.append([0, 1, 0])
matriks.append([0, 0, 1])
print(matriks)
