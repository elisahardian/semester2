## LAT 3. PENUKARAN POSISI SUNGLE LINKED LIST. BERDASARKAN INPUTAN USER

array=[42, 57, 23, 51]
print("list saat ini: ", array)
a=int(input("input posisi elemen pertama yg ditukar: "))
b=int(input("input posisi elemen kedua yg ditukar: "))
if a<0 or b<0 or a>=len(array) or b>=len(array):
    print("posisi yang diinput tidak valid")
def tukar(array):
  array[a], array[b]=array[b], array[a]
  return array
print("List setelah ditukar: ", tukar(array))
#cara yg di atas ini bisa

print("-"*20)
#cara yang dibawah ini bisa
my_list = [42, 57, 23, 51]

print("list saat ini: ", end="")
for x in my_list:
    print(x, end=" ")
print()

pos1 = int(input("masukkan posisi elemen pertama yang akan ditukar (0-based): "))
pos2 = int(input("masukkan posisi elemen kedua yang akan ditukar (0-based): "))

if pos1 < 0 or pos1 >= len(my_list) or pos2 < 0 or pos2 >= len(my_list):
    print("Posisi yang dimasukkan tidak valid.")
    exit(1)

my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]

print("List setelah ditukar: ", end="")
for x in my_list:
    print(x, end=" ")
print()
exit(0)