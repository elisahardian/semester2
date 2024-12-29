## NON OBJEK. 
# PROGRAM 1: MENGHITUNG LUAS SEGITIGA
#mendeklarasikan variable 
alas= int(input("masukkan alas: "))
tinggi= int(input("masukkan tinggi: "))
#hitung luas
luas=0.5*alas*tinggi
#cetak
print("luas segitiga: ", luas)


## NON OBJEK.
# PROGRAM 2: MENGHITUNG LUAS SEGITIGA. DENGAN PROSEDUR TANPA PARAMETER
#membuat prosedur tanpa parameter
def hitung():
    alas=int(input("masukkan alas: "))
    tinggi=int(input("masukkan tinggi: "))
    luas=0.5*alas*tinggi
    print("luas segitiga: ", luas)
#program utama
def main():
    #memanggil prosedur
    hitung()
main()


# NON OBJEK.
# PROGRAM 3: MENGHITUNG LUAS SEGITIGA. DENGAN PROSEDUR DENGAN PARAMETER
#membuat prosedur dengan parameter
def hitung(alas, tinggi):
    luas=0.5*alas*tinggi
    print("luas segitiga: ", luas)
#program utama
def main():
    #memanggil prosedur
    alas=int(input("masukkan alas: "))
    tinggi=int(input("masukkan tinggi: "))
    hitung(alas, tinggi)
main()
