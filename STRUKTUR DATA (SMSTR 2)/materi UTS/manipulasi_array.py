m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(m)
print(m[0])
print(m[5])
print("panjang mula mula: ", len(m))
for i in range(0, 9):
    print(m[i], end=" ")
print("\n")
for i in m:
    print(i)
print()
m.append(10)  #menambahkan data
for i in range(0, 10):
    print(m[i], end=" ")
print(";panjang array sekarang: ", len(m))
print()
m.pop(9)
for i in range(0, len(m)):
    print(m[i], end=" ")
print(";panjang array sekarang: ", len(m))
print()
m.pop(5)
for i in range(0, len(m)):
    print(m[i], end=" ")
print(";panjang array sekarang: ", len(m))
print()
m.insert(5, 100) # di posisi index ke 5, ditambahin angka 100
print(m)
m[3] = 99 # di posisi index 3 diganti dengan angka 99
print(m)
m.sort() # diurutkan kecil besar
print(m)
m.reverse() # urutan dibalik
print(m)
m.pop(5) # menghapus index ke 5
print(m)
m.remove(1) # menghapus data yang bernilai 1
print(m)
n = [56, 67, 89]
m.extend(n) #menambahkan list sebuah list
print(m)
