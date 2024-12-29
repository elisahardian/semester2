## PROGRAM MEMBUAT DATA DOKTER. DENGAN FUNGSI, TANPA PARAMETER, PUBLIC
#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat method dengan fungsi tanpa parameter
    #metode tunjangan
    def tunjangan(self):
        return 0.1 * self.gaji
    #method total gaji
    def totalGaji(self):
        return self.tunjangan() + self.gaji
#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter(None, None, None)
    objDokter.id = str(input("masukkan id\t: "))
    objDokter.nama = str(input("masukkan nama\t: "))
    objDokter.gaji = int(input("masukkan gaji\t: "))
    print("Tunjangan\t: ", objDokter.tunjangan())
    print("Total Gaji\t: ", objDokter.totalGaji())
main()

