"""
[42, 57, 23, 51]
tukar posisi list berdasarkan inputan user

output:
List saat ini: 42, 57, 23, 51
input posisi elemen pertama yang ditukar
input posisi elemen keuda yang ditukar
List saat ini........ -> setelah ditukar
"""
# List awal
list = [42, 57, 23, 51]

# Menampilkan list saat ini
print("List saat ini:", ", ".join(str(x) for x in list))

# Meminta input dari pengguna
pos1=int(input("Masukkan posisi elemen pertama yang akan ditukar (0-based):"))
pos2=int(input("Masukkan posisi elemen kedua yang akan ditukar (0-based):"))

# Menukar posisi elemen
list[pos1], list[pos2] = list[pos2], list[pos1]

# Menampilkan list setelah ditukar
print("List setelah ditukar:", ", ".join(str(x) for x in list))
