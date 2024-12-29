## NON OBJEK.
# PROGRAM 4: MENGHITUNG LUAS SEGITIGA. DENGAN FUNGSI TANPA PARAMETER
#membuat fungsi tanpa parameter
def hitung():
    alas=int(input("masukkan alas: "))
    tinggi=int(input("masukkan tinggi: "))
    luas=0.5*alas*tinggi
    return luas
#program utama
def main():
    #memanggil fungsi
    print("luas segitiga: ", hitung())
main()


## NON OBJEK.
# PROGRAM 5: MENGHITUNG LUAS SEGITIGA. DENGAN FUNGSI DENGAN PARAMETER
#membuat fungsi dengan parameter
def hitung(alas, tinggi):
    luas=0.5*alas*tinggi
    return luas
#program utama
def main():
    alas=int(input("masukkan alas: "))
    tinggi=int(input("masukkan tinggi: "))
    #memanggil fungsi
    print("luas segitiga: ", hitung(alas, tinggi))
main()
