## PEMROGRAMAN BERORIENTASI OBJEK.
# PROGRAM 6: MENGHITUNG LUAS SEGITIGA. DENGAN FUNGSI, TANPA PARAMETER, PUBLIC
#membuat kelas
class Segitiga:
  #membuat konstruktor
  def __init__(self, alas, tinggi):
    self.alas= alas
    self.tinggi= tinggi

  #membuat method dengan fungsi tanpa parameter
  def hitung(self):
    return 0.5 * self.alas * self.tinggi

#program utama
def main():
  #instansiasi kelas menjadi objek
  objSegitiga= Segitiga(None, None)
  objSegitiga.alas=int(input("masukkan alas \t: "))
  objSegitiga.tinggi=int(input("masukkan tinggi \t: "))
  print("Luas segitiga \t: ", objSegitiga.hitung())
main()


## PEMROGRAMAN BERORIENTASI OBJEK.
# PROGRAM 7: MENGHITUNG LUAS SEGITIGA. DENGAN FUNGSI, DENGAN PARAMETER, PUBLIC
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    #membuat method dengan fungsi beserta parameter
    def hitung(self, alas, tinggi):
        return 0.5 * alas * tinggi
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
    objSegitiga.alas = int(input("masukkan alas\t: "))
    objSegitiga.tinggi = int(input("masukkan tinggi\t: "))
    print("luas segitiga\t: ", objSegitiga.hitung(objSegitiga.alas, objSegitiga.tinggi))
main()
