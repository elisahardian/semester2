## PROGRAM MEMBUAT DATA DOKTER. DENGAN FUNGSI, DENGAN PARAMETER, PUBLIC
#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat method dengan fungsi dengan parameter
    #metode tunjangan
    def tunjangan(self, gaji):
        return 0.1 * self.gaji
    #method total gaji
    def totalGaji(self, gaji):
        return self.tunjangan(self.gaji) + self.gaji
#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter(None, None, None)
    objDokter.id = str(input("masukkan id\t: "))
    objDokter.nama = str(input("masukkan nama\t: "))
    objDokter.gaji = int(input("masukkan gaji\t: "))
    print("Tunjangan\t: ", objDokter.tunjangan(objDokter.tunjangan(objDokter.gaji)))
    print("Total Gaji\t: ", objDokter.totalGaji(objDokter.totalGaji(objDokter.gaji)))
main()

