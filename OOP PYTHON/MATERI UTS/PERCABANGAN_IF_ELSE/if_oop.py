"""
#program if mahasiswa
#membuat kelas beserta konstruktornya
class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai
    #membuat method
    def hitung(self, nilai):
        if (self.nilai >= 60):
            print("keterangan\t: anda lulus")
#membuat blok main program
def main():
    #instansiasi kelas menjadi objek
    objMahasiswa = Mahasiswa(None, None, None)
    objMahasiswa.nim= str(input("masukkan nim\t: "))
    objMahasiswa.nama= str(input("masukkan nama\t: "))
    objMahasiswa.nilai= int(input("mauskkan nilai\t: "))
    objMahasiswa.hitung(objMahasiswa.nilai)
main()
"""

class Mahasiswa:
    #membuat kontruktor
    def __init__ (self, nim, nama, nilai):
        self.nim=nim
        self.nama=nama
        self.nilai=nilai
    #membuat method dengan fungsi
    def hitung(self, nilai):
        if (nilai>=60):
            return ('ketetrangan\t: anda lulus')
        else:
            return ('keterangan\t: anda tidak lulus')
#blok main program
def main():
    #instansiasi kelas menjadi objek
    objMahasiswa = Mahasiswa(None, None, None)
    objMahasiswa.nim= str(input("masukkan nim\t:"))
    objMahasiswa.nama= str(input("masukkan nama\t:"))
    objMahasiswa.nilai= int(input("masukkan nilai\t:"))
    print(objMahasiswa.hitung(objMahasiswa.nilai))
main()


