## PEMROGRAMAN BERORIENTASI OBJEK
# PROGRAM 12: MEMBUAT LUAS SEGITIGA. DENGAN PROSEDUR, TANPA PARAMETER, PUBLIC
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    #membuat method dengan fungsi tanpa nilai balikan (prosedur)
    #tanpa parameter
    def hitung(self):
        luas = 0.5 * self.alas * self.tinggi
        print("luas segitiga\t: ", luas)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
    objSegitiga.alas = int(input("masukkan alas\t: "))
    objSegitiga.tinggi = int(input("masukkan tinggi\t: "))
    objSegitiga.hitung()
main()


## PEMROGRAMAN BERORIENTASI OBJEK
# PROGRAM 13: MEMBUAT LUAS SEGITIGA. DENGAN PROSEDUR, DENGAN PARAMETER, PUBLIC
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    #membuat method dengan fungsi tanpa nilai balikan (prosedur)
    #dengan parameter
    def hitung(self, alas, tinggi):
        luas = 0.5 * alas * tinggi
        print("luas segitiga\t: ", luas)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
    objSegitiga.alas = int(input("masukkan alas\t: "))
    objSegitiga.tinggi = int(input("masukkan tinggi\t: "))
    objSegitiga.hitung(objSegitiga.alas, objSegitiga.tinggi) 
main()       
