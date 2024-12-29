## PROGRAM MEMBUAT DATA DOKTER. DENGAN PROSEDUR, TANPA PARAMETER, PUBLIC
#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat method dengan prosedur tanpa parameter
    def tunjangan(self):
        tun = 0.1 * self.gaji
        print("Tunjangan\t: ", tun)
    def totalGaji(self):
        total = (0.1 * self.gaji) + self.gaji
        print("Total Gaji\t: ", total)
#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter= Dokter(None, None, None)
    objDokter.id=str(input("masukkan id\t: "))
    objDokter.nama=str(input("masukkan nama\t: "))
    objDokter.gaji=int(input("masukkan gaji\t: "))
    objDokter.tunjangan()
    objDokter.totalGaji()
main()      
