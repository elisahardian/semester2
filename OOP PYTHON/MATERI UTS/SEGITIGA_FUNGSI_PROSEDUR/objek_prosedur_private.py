## PEMROGRAMAN BERORIENTASI OBJEK
# PROGRAM 10: MEMBUAT LUAS SEGITIGA. DENGAN PROSEDUR, TANPA PARAMETER, PRIVATE
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self, __alas, __tinggi):
        self.__alas = __alas
        self.__tinggi = __tinggi
    #menerapkan property method
    def setAlas(self, __alas):
        self.__alas = __alas
    def getAlas(self):
        return self.__alas
    def setTinggi(self, __tinggi):
        self.__tinggi = __tinggi
    def getTinggi(self):
        return self.__tinggi
    #membuat method dengan fungsi tanpa nilai balikan (prosedur)
    #tanpa parameter
    def hitung(self):
        luas = 0.5 * self.__alas * self.__tinggi
        print("luas segitiga\t: ", luas)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
    objSegitiga.setAlas(int(input("masukkan alas\t: ")))
    objSegitiga.setTinggi(int(input("masukkan tinggi\t: ")))
    objSegitiga.hitung()
main()


## PEMROGRAMAN BERORIENTASI OBJEK
# PROGRAM 11: MEMBUAT LUAS SEGITIGA. DENGAN PROSEDUR, DENGAN PARAMETER, PRIVATE
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self, __alas, __tinggi):
        self.__alas = __alas
        self.__tinggi = __tinggi
    #menerapkan property method dengan set dan get
    def setAlas(self, __alas):
        self.__alas = __alas
    def getAlas(self):
        return self.__alas
    def setTinggi(self, __tinggi):
        self.__tinggi = __tinggi
    def getTinggi(self):
        return self.__tinggi
    #membuat method dengan fungsi tanpa nilai balikan (prosedur)
    #dengan parameter
    def hitung(self, alas, tinggi):
        luas = 0.5 * alas * tinggi
        print("luas segitiga\t: ", luas)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
    objSegitiga.setAlas(int(input("masukkan alas\t: ")))
    objSegitiga.setTinggi(int(input("masukkan tinggi\t: ")))
    objSegitiga.hitung(objSegitiga.getAlas(), objSegitiga.getTinggi())
main()
