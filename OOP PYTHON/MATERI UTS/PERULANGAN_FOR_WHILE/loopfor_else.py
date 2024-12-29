"""
# for else

for i in range(0,5):
    print(i)
else:
    print("proses loop selesai")
"""


#for.. else+break
listdosen=['Tina', 'Erna', 'Lili', 'Wati', 'Lusi', 'Diky', 'Angga', 'Renaldi', 'Juliet', 'Fera']
caridata=input("masukkan nama dosen yang dicari: ")
for i, nama in enumerate(listdosen):
    if nama.lower() == caridata.lower(): #semua dianggap huruf kecil semua
        print("data dosen ada pada index ke: ", i)
        break
else:
    print("nama dosen yang dicari tidak ada")
