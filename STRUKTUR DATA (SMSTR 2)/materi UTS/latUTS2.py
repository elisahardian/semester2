## PROGRAM TUKAR POSISI LIST BERDASARAKN INPUTAN USER. (PYTHON)
#LIST = [42, 57, 23, 51]

#cara 1
my_list = [42, 57, 23, 51]
print("list saat ini: ", end=" ")
for x in my_list:
    print(x, end=" ")
print()
pos1=int(input("masukkan posisi elemen pertama yang akan ditukar(0-based): "))
pos2=int(input("masukkan posisi elemen kedua yang akan ditukar(0-based): "))
if pos1 < 0 or pos1 >= len(my_list) or pos2 < 0 or pos2 >= len(my_list):
    print("posisi yang dimasukkan tidak valid")
    exit(1)
my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
print("list setelah ditukar: ", end=" ")
for x in my_list:
    print(x, end=" ")
print()
exit(1)

#cara 2
array = [42, 57, 23, 51]
print("list saat ini: ", array)
a= int(input("masukkan posisi elemen pertama yang akan ditukar(0-based): "))
b= int(input("masukkan posisi elemen kedua yang akan ditukar(0-based): "))
if a < 0 or b < 0 or a >= len(array) or b >= len(array):
    print("posisi yang diinputkan tidak valid")
def tukar(mu_list):
    array[a], array[b] = array[b], array[a]
    return array
print("list setelah ditukar: ", array)
