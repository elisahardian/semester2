"""
## FAKTORIAL MENGGUNAKAN REKURSIF
def faktorial(n):
    if (n==1):
        return 1
    else:
        return n * faktorial(n-1)
n = int(input("masukkan n faktorial: "))
print(f"{n}! = ", faktorial(n))

## DERET FIBONACCI MENGGUNAKAN REKURSIF
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
x=int(input("batas deret fibonacci: "))
print("deret fibonacci: ")
for i in range(x):
    print(fibonacci(i), end=" ")

## MIN MAX DENGAN DIVIDE AND CONQUER
dat = [60, 42, 53, 10, 4, 60, 89]
terendah = dat[0]
tertinggi = dat[0]
def minmaxs(awal, akhir, minr, maxr):
    global terendah, tertinggi
    if (awal >= akhir):
        terendah = dat[awal]
        tertinggi = dat[akhir]
    else:
        tengah = int(awal + (akhir - awal)/2)
        minmaxs(awal, tengah, terendah, tertinggi)
        minmaxs(tengah + 1, akhir, terendah, tertinggi)
    if (terendah > minr):
        terendah = minr
    if (tertinggi < maxr):
        tertinggi = maxr
#main program
panjang = len(dat)
minmaxs(0, panjang-1, dat[0], dat[0])
print("minimum: ", terendah)
print("maximum: ", tertinggi)

## HITUNG PANGKAT DENGAN REKURSIF
def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat-1)
    else:
        return bilangan
bilangan= int(input("masukkan bilangan: "))
pangkat= int(input("masukkan pangkat: "))
hasil = hitung_pangkat(bilangan, pangkat)
print(f"hasil = {hasil}")
"""
"""
## PROGRAM MENGURUTKAN BERDASARKAN NIM MENGGUNAKAN ALGORITMA SELECTION SORT. BESERTA OUTPUT NAMANYA
def selection_sort(nim_list, nama_list):
    n = len(nim_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nim_list[j] < nim_list[min_idx]:
                min_idx = j
        nim_list[i], nim_list[min_idx] = nim_list[min_idx], nim_list[i]
        nama_list[i], nama_list[min_idx] = nama_list[min_idx], nama_list[i]
nim_list = [103, 102, 130, 122, 128, 119]
nama_list = ['budi', 'ayu', 'canie', 'wati', 'bagas', 'nino']
print("data sebelum diurutkan: ")
for i in range(len(nim_list)):
    print("NIM: ", nim_list[i], ";\tNama: ", nama_list[i])
    print("-"*20)
selection_sort(nim_list, nama_list)
print("data setelah diurutkan berdasarkan nim: ")
for i in range(len(nim_list)):
    print("NIM: ", nim_list[i], ";\tNama: ", nama_list[i])
    print("-"*20)

## PROGRAM MENCARI DAN MENAMPILKAN DATA NIM DENGAN NAMA "NINO". DENGAN LINEAR SEARCH
def linear_search(nama_list, nim_list, target_nama):
    for i in range(len(nama_list)):
        if nama_list[i] == target_nama:
            return nim_list[i]
    return None
nim_list = [103, 102, 130, 122, 128, 119]
nama_list = ['budi', 'ayu', 'canie', 'wati', 'bagas', 'nino']
target_nama = "nino"
result_nim = linear_search(nama_list, nim_list, target_nama)
if result_nim:
    print("NIM", target_nama, "adalah", result_nim)
else:
    print("tidak ditemukan")

## PRGORAM MENCARI DAN MENAMPILKAN DATA NAMA DENGAN NIM 122. DENGAN LINEAR SEARCH
def linear_search(nama_list, nim_list, target_nim):
    for i in range(len(nim_list)):
        if nim_list[i] == target_nim:
            return nama_list[i]
    return None
nim_list = [103, 102, 130, 122, 128, 119]
nama_list = ['budi', 'ayu', 'canie', 'wati', 'bagas', 'nino']
target_nim = 122
result_nama = linear_search(nama_list, nim_list, target_nim)
if result_nama:
    print("NIM", result_nama, "adalah", target_nim)
else:
    print("tidak ditemukan")
"""
"""
## ALGORITMA DIVIDE AND CONQUER UNTUK MENEMUKAN NIM TERTINGGI DAN TERENDAH, BESERTA NAMANYA

def find_min_max(nama_list, nim_list, start, end):
    if start == end:
        return nim_list[start], nim_list[start], nama_list[start], nama_list[start]
    mid = (start + end)//2
    min_left, max_left, min_name_left, max_name_left = find_min_max(nama_list, nim_list, start, mid)
    min_right, max_right, min_name_right, max_name_right = find_min_max(nama_list, nim_list, mid + 1, end)
    min_nim = min(min_left, min_right)
    max_nim = max(max_left, max_right)

    if min_left == min_right:
        min_name = min_name_left
    elif min_left < min_right:
        min_name = min_name_left
    else:
        min_name = min_name_right
    
    if max_left == max_right:
        max_name = max_name_left
    elif max_left > max_right:
        max_name = max_name_left
    else:
        max_name = max_name_right
    return min_nim, max_nim, min_name, max_name
nim_list = [103, 102, 130, 122, 128, 119]
nama_list = ['budi', 'ayu', 'canie', 'wati', 'bagas', 'nino']
min_nim, max_nim, min_name, max_name = find_min_max(nama_list, nim_list, 0, len(nim_list)-1)
print("NIM terendah: ", min_nim, ", Nama: ", min_name)
print("NIM tertinggi: ", max_nim, ", Nama: ", max_name)
"""

"""
## PROSEDUR REKURSIF BARISAN ARITMATIKA(0, n). RUMUS = Un= a+(n-1)b. a=15, b=5. OUTPUT BARISAN 0 SAMPE n
def barisan_aritmatika(a, b, n):
    if n == 0:
        return []
    else:
        barisan_sebelumnya = barisan_aritmatika(a, b, n-1)
        barisan_sebelumnya.append(a + (n-1) * b)
        return barisan_sebelumnya
a=int(input("a= "))
b=int(input("b= "))
n=int(input("berapa banyak hasil yg ingin dicetak: "))
barisan = barisan_aritmatika(a, b, n)
print("barisan aritmatika (0, n) dengan a=", a, ",b=", b, "sampai", n, "elemen adalah: ", barisan)

## PROSEDUR REKURSIF DERET GEOMETRI(0, n). RUMUS = Un=ar^(n-1). a=3, r=2. OUTPUT BARISAN 0 SAMPE n
def barisan_geometri(a, r, n):
    if n == 1:
        return [a]
    else: 
        barisan_sebelumnya = barisan_geometri(a, r, n-1)
        barisan_sebelumnya.append(a * (r ** (n-1)))
        return barisan_sebelumnya
a=int(input("a= "))
r=int(input("r= "))
n=int(input("berapa banyak hasil yg ingin dicetak: "))
barisan = barisan_geometri(a, r, n)
print("barisan geometri (0, n) dengan a=", a, ",r=", r, "sampai", n, "elemen adalah: ", barisan)
"""


##PROGRAM REKURSIF UNTUK MENGHITUNG TOTAL NILAI DAN JUMLAH NILAI DALAM ARRAY
def hitung_total(arr, idx):
    if idx < 0:
        return 0
    else:
       return arr[idx] + hitung_total(arr, idx - 1)
array = [15, 8, 19, 20, 10, 22, 35, 100]
total = hitung_total(array, len(array)-1)
print("total nilai dalam array: ", total)
print()

def hitung_total(arr, idx=0): #index mulai dari 0
    if idx == len(arr): #jika index sepanjang array. return 0
        return 0
    else:
       return arr[idx] + hitung_total(arr, idx + 1) #index bertambah dari sini
array = [ 15, 2, 4, 3, 11, 5]
total = hitung_total(array)
print("total nilai dalam array: ", total)