#if bersarang

#membuat kelas
class Mahasiswa:
    #membuat konstruktor
    def __init__ (self, nim, nama, nilai):
        self.nim=nim
        self.nama=nama
        self.nilai=nilai
    #membuat method dengan fungsi
    def hitung(self, nilai):
        if (nilai >= 80) and (nilai <= 100):
            return ("Grade nilai\t: A")
        elif (nilai >= 60) and (nilai < 80):
            return ("Grade nilai\t: B")
        elif (nilai >= 40) and (nilai < 60):
            return ("Grade nilai\t: C")
        elif (nilai >= 20) and (nilai < 40):
            return ("Grade nilai\t: D")
        else:
            return ("Grade nilai\t: Di luar ketentuan")
#blok main program
def main():
    #instansiasi kelas menjadi objek
    objMahasiswa = Mahasiswa(None, None, None)
    objMahasiswa.nim = str(input("masukkan nim\t: "))
    objMahasiswa.nama = str(input("masukkan nama\t: "))
    objMahasiswa.nilai = int(input("masukkan nilai\t: "))
    print(objMahasiswa.hitung(objMahasiswa.nilai))
main()
