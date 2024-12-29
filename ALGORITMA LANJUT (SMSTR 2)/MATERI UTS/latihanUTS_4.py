## dengan algoritma binary search untuk mencari dan menampilkan data mahasiswa dengan nim 234. berdasarkan data
mahasiswa = [{"nim":234, "umur":17},
              {"nim":567, "umur":18},
              {"nim":856, "umur":20},
              {"nim":123, "umur":17},
              {"nim":555, "umur":23},
              {"nim":642, "umur":17},
              {"nim":792, "umur":17},
              {"nim":415, "umur":21},
              {"nim":156, "umur":22},
              {"nim":729, "umur":19}]
nim_list = [234, 567, 856, 123, 555, 642, 792, 415, 156, 729]
umur_list = [17, 18, 20, 17, 23, 17, 17, 21, 22, 19]

"""
#ini kalau yg langsung dari dictionary
def binary_search(mahasiswa, target_nim):
    left = 0
    right = len(mahasiswa) - 1
    while left <= right:
        mid = (left + right)//2
        if mahasiswa[mid]["nim"]==target_nim:
            return mahasiswa[mid]
        elif mahasiswa[mid]["nim"]<target_nim:
            left = mid + 1
        else:
            right = mid - 1
    return None

target_nim = 234
result = binary_search(mahasiswa, target_nim)
if result:
    print("Data mahasiswa dengan NIM", target_nim, "ditemukan" )
    print("NIM: ", result["nim"], "\nUmur: ", result["umur"])
else:
    print("data mahasiswa dengan nim", target_nim, "tidak ditemukan")
"""

"""
## dengan algoritma binary search untuk mencari dan menampilkan data mahasiswa dengan nim 234. berdasarkan data
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
nim_list = [234, 567, 856, 123, 555, 642, 792, 415, 156, 729]
umur_list = [17, 18, 20, 17, 23, 17, 17, 21, 22, 19]
target = 234
result = binary_search(nim_list, target)
if result != -1:
    print("NIM: ", target, "\nUmur: ", umur_list[result])
else:
    print("data tak sesuai")

## dengan algoritma binary search untuk mencari dan menampilkan data mahasiswa dengan umur 23. berdasarkan data
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
nim_list = [234, 567, 856, 123, 555, 642, 792, 415, 156, 729]
umur_list = [17, 18, 20, 17, 23, 17, 17, 21, 22, 19]
target = 23
result = binary_search(umur_list, target)
if result != -1:
    print("NIM: ", nim_list[result], "\nUmur: ", target)
else:
    print("data tak sesuai")

## dengan algoritma binary search untuk mencari dan menampilkan data mahasiswa dengan nama ="illona". berdasarkan data
mahasiswa = [{"nim":234, "umur":17, "nama": 'abigail'},
              {"nim":567, "umur":18, "nama": 'bennise'},
              {"nim":856, "umur":20, "nama": 'charles'}, 
              {"nim":123, "umur":17, "nama": 'denis'},
              {"nim":555, "umur":23, "nama": 'elena'},
              {"nim":642, "umur":17, "nama": 'flora'},
              {"nim":792, "umur":17, "nama": 'ganny'},
              {"nim":415, "umur":21, "nama": 'hammy'},
              {"nim":156, "umur":22, "nama": 'illona'},
              {"nim":729, "umur":19, "nama": 'jacko'}]
def binary_search(mahasiswa, target_nama):
    left = 0
    right = len(mahasiswa) - 1
    while left <= right:
        mid = (left + right)//2
        if mahasiswa[mid]["nama"]==target_nama:
            return mahasiswa[mid]
        elif mahasiswa[mid]["nama"]<target_nama:
            left = mid + 1
        else:
            right = mid - 1
    return None

target_nama = "illona"
result = binary_search(mahasiswa, target_nama)
if result:
    print("Data mahasiswa dengan nama", target_nama, "ditemukan" )
    print("NIM: ", result["nim"], "\nUmur: ", result["umur"], "\nNama: ", result["nama"])
else:
    print("data mahasiswa dengan nama", target_nama, "tidak ditemukan")


## PROSEDUR REKURSIF DERET (0, n) UNTUK MENAMPILKAN DERET BILANGAN. RUMUS Un = ar**(n-1). dengan a=3, r=2. tampilkan 0 s/d n

#cara1
a=3
r=2
def rekursif(n, current=1):
    if current < n:
        print(a * (r** (current -1)), end=" ")
        rekursif(n, current + 1)
n = int(input("banyak ditampilkan: "))
rekursif(n+1)

#cara2
def deret(a, r, n):
    if n == 0:
        return a
    else:
        return a*r**(n-1) + deret(a, r, n-1)
def main():
    a=3
    r=2
    n= int(input("masukkan nilai n untuk menampilkan deret (0-n): "))
    print("deret bilangan: ")
    for i in range(n+1):
        print(deret(a,r,i), end=" ")
if __name__ == "__main__":
    main()
"""

## FUNGSI REKURSIF TERKECIL UNTUK MENCARI NILAI TERKECIL. data = [40, 45, 7]
def terkecil(data, n):
    if n == 1:
        return data[0]
    else:
        smallest = terkecil(data, n-1)
        return min(smallest, data[n-1])
def main():
    data=[40, 45, 7]
    n = len(data)
    smallest = terkecil(data, n)
    print("nilai terkecil dalam array: ", smallest)
main()

## FUNGSI REKURSIF TERBESAR UNTUK MENCARI NILAI TERBESAR. data = [40, 45, 7]
def terbesar(data, n):
    if n == 1:
        return data[0]
    else:
        biggest = terbesar(data, n-1)
        return max(biggest, data[n-1])
def main():
    data = [40, 45, 7]
    n = len(data)
    biggest = terbesar(data, n)
    print("nilai terbesar dalam array: ", biggest)
main()
