# LAT 1
## LATIHAN MENERAPKAN INSTANCE METHOD
#LATIHAN DOKTER

#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__ (self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat method instance dengan fungsi beserta parameter
    #method instant tunjangan
    def tunjangan(self, gaji):
        return 0.1 * gaji
    #method intant total gaji
    def totalGaji(self, gaji):
        return self.tunjangan(self.gaji) + gaji

#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter (None, None, None)
    objDokter.id = str(input("Masukkan id\t: "))
    objDokter.nama = str(input("Masukkan nama\t: "))
    objDokter.gaji = int(input("Masukkan gaji\t: "))
    print("Tunjangan\t: ", objDokter.tunjangan(objDokter.gaji))
    print("Total gaji\t: ", objDokter.totalGaji(objDokter.gaji))

main()
