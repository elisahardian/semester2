"""
##BUBBLE SORT
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
arr=[64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("sorted array (bubble sort): ", arr)

##INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        print(arr)
arr=[64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("sorted array (insertion sort): ", arr)

##SELECTION SORT
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
arr=[64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("sorted array (selection sort): ", arr)
"""            

## LATIHAN UTS ##

nim_list=[109, 107, 115, 100, 111, 104, 114, 103, 102, 105, 110, 112, 101]
nama_list=["jonathan", "steven", "vinnzene", "marcelino", "kwik", "samuel", "kenisha", "albert", "pheremya", "alvito", "chrisna", "fricilia", "antonio"]

#mengurutkan nim berdasarkan algoritma selection
"""
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        nama_list[i], nama_list[min_idx] = nama_list[min_idx], nama_list[i]
        print("NIM: ", arr[i], "; Nama: ", nama_list[i])
arr=[109, 107, 115, 100, 111, 104, 114, 103, 102, 105, 110, 112, 101]
selection_sort(arr)
"""
"""
#atau bisa juga
def selection_sort(nim, nama):
    n=len(nim)
    for i in range(n):
        #temukan index minimum dalam sisa daftar
        min_index = i
        for j in range(i+1, n):
            if nim[j] < nim[min_index]:
                min_index = j
        #tukar elemen minimum dengan elemen pertama dalam sisa daftar
        nim[i], nim[min_index] = nim[min_index], nim[i]
        nama[i], nama[min_index] = nama[min_index], nama[i]
selection_sort(nim_list, nama_list)
for i in range(len(nim_list)):
    print("="*15)
    print("Nama: ", nama_list[i], "\nNIM: ", nim_list[i])
"""


#mencari dan menampilkan data nim dengan nama "pheremya" dengan algoritma linear search
"""
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #return index jika target ditemukan
    return -1 #return -1 jika target tidak ditemukan

target="pheremya"
result = sequential_search(nama_list, target)
print("NAMA: ", target, "\nNIM: ", nim_list[result])

#mencari dan menampilkan data nama dengan nim 114 dengan algoritma linear search
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #return index jika target ditemukan
    return -1 #return -1 jika target tidak ditemukan

target=114
result = sequential_search(nim_list, target)
print("NAMA: ", nama_list[result], "\nNIM: ", target)
"""

"""
# NIM DAN NAMA YANG TERENDAH DAN TERTINGGI 
#sebelum menjalankan kode yg ini, harus dijalan kan dulu yg mengurutkan nama nim dari terendah ke tertinggi. kalo ga diurutkan dulu nimnya, hasilnya beda lagi.
terendah = nim_list[0]
tertinggi = nim_list[0]

def minmaxs(awal, akhir, minr, maxr, awal_out, akhir_out):
  global terendah, tertinggi
  if (awal >= akhir):
    terendah = nim_list[awal]
    tertinggi = nim_list[akhir]
    awal_out = awal
    akhir_out = akhir
  else:
    tengah = int(awal + (akhir - awal)/2)
    minmaxs(awal, tengah, terendah, tertinggi, awal_out, akhir_out)
    minmaxs(tengah+1 ,akhir, terendah, tertinggi, awal_out, akhir_out)
  if (terendah > minr):
    terendah = minr
  if (tertinggi < maxr):
    tertinggi = maxr
  return awal_out, akhir_out
# Contoh penggunaan
awal = 0
akhir = len(nim_list) - 1
# Memanggil fungsi minmaxs dengan 6 argumen
awal_out, akhir_out = minmaxs(awal, akhir, terendah, tertinggi, awal, akhir)
print("NIM Terendah : ", terendah, "\nNama : " , nama_list[awal_out])
print("NIM Tertinggi: ", tertinggi, "\nNama : ", nama_list[akhir_out])
"""
"""
#membuat DERET ARITMATIKA dengan rumus Un=a+(n-1)b. dengan a=15, b=5
def rekursi(n, current = 0): #dimuai dari un, n (current) nya itu 0. u0=15+(-5)
    if current < n:
        print(15 + (current -1) * 5, end=" ")
        rekursi(n ,current+1)
rekursi(5)


#fungsi REKURSIF untuk menghitung JUMLAH NILAI dan jumlah nilai dalam array=[15, 8, 19, 20, 10, 22, 35, 100]
dataarray=[15, 8, 19, 20, 10, 22, 35, 100]
def recursive_sum(arr, index=0):
    if index == len(arr): #jika index sudah sampai sepanjang arraynya. return 0
        return 0
    else:
        return arr[index] + recursive_sum(arr, index + 1) #index akan terus bertambah disini. index +1
total_sum = recursive_sum(dataarray)
print("jumlah total dari array: ", total_sum)

"""

## DIVIDE AND CONQUER
#min max dengan DnC
dat = [60, 74, 55, 4, 650, 60, 82, 51, 71, 66, 330, 91]
terendah = dat[0]
tertinggi = dat[0]
def minmax(awal, akhir, minr, maxr):
    global terendah, tertinggi
    if (awal >= akhir):
        terendah = dat[awal]
        tertinggi = dat[akhir]
    else:
        tengah = int(awal + (akhir - awal) / 2)
        minmax(awal, tengah, terendah, tertinggi)
        minmax(tengah+1, akhir, terendah, tertinggi)
    if (terendah > minr):
        terendah = minr
    if (tertinggi < maxr):
        tertinggi = maxr
#main program
panjang = len(dat)
minmax(0, panjang-1, dat[0], dat[0])
print("minimum: ", terendah)
print("maximum: ", tertinggi)
