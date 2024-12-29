## PROGRAM MEMBUAT DATA DOKTER. DENGAN PROSEDUR, DENGAN PARAMETER, PUBLIC
#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat method dengan prosedur dengan parameter
    def tunjangan(self, gaji):
        tun = 0.1 * gaji
        print("tunjangan\t: ", tun)
    def totalGaji(self, gaji):
        total = (0.1 * gaji) + gaji
        print("total gaji\t: ", total)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter(None, None, None)
    objDokter.id=str(input("masukkan id\t: "))
    objDokter.nama=str(input("masukkan nama\t: "))
    objDokter.gaji=int(input("masukkan gaji\t: "))
    objDokter.tunjangan(objDokter.gaji)
    objDokter.totalGaji(objDokter.gaji)
main()
