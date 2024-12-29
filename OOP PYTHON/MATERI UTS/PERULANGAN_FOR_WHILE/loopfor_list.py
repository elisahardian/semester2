#FOR DENGAN LIST

"""
#membuat list

listNamaBulan=['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
for Bulan in listNamaBulan:
    print(Bulan)
"""

"""
#untuk mengetahui urutan list denan memanggil index dengan: enumerate(...)

listNamaBulan=['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
for i, Bulan in enumerate(listNamaBulan):
    print(i, Bulan)
"""

#for dengan fungsi range()

for i in range(5):
    print('i = ' + str(i) + ', perulangan ke: ' + str(i+1))

