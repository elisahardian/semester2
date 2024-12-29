# LAT 2
## LATIHAN MENERAPKAN STATIC METHOD, INSTANCE ATRIBUT
#LATHIAN DOKTER

#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id # instance variabel
        self.nama = nama #instance variabel
        self.gaji = gaji #instance variabel
    #membuat method static dengan fungi beserta parameter
    #method tunjangan
    @staticmethod
    def tunjangan(gaji):
        return 0.1 * gaji
    #method total gaji
    @staticmethod
    def totalGaji(gaji):
        return gaji + Dokter.tunjangan(gaji)
#program utama
def main():
    #instansiasi kelas menjadi objek untuk membaca atribut ( yg bukan static )
    objDokter = Dokter(None, None, None)
    objDokter.id = str(input("Masukkan id\t: "))
    objDokter.nama = str(input("Masukkan nama\t: "))
    objDokter.gaji = int(input("Masukkan gaji\t: "))
    print("Tunjangan\t: ", Dokter.tunjangan(objDokter.gaji))
    print("Total gaji\t: ", Dokter.totalGaji(objDokter.gaji))
main()