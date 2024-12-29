# LAT 4
## LATIHAN MENERAPKAN CLASS METHOD
#LATIHAN DOKTER

#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #membuat class method tunjangan
    #class method tunjangan
    @classmethod
    def tunjangan(cls, gaji):
        return 0.1 * gaji
    #class method total gaji
    @classmethod
    def totalGaji(cls, tunjangan, gaji):
        return cls.tunjangan(gaji)+gaji
#main program
def main():
    #instansasi kelas menjadi objek
    objDokter = Dokter (None, None, None)
    objDokter.id = str(input("Masukkan id\t: "))
    objDokter.nama = str(input("Masukkan nama\t: "))
    objDokter.gaji = int(input("Masukkan gaji\t: "))
    print("Tunjangan\t: ", objDokter.tunjangan(objDokter.gaji))
    print("Total gaji\t: ", objDokter.totalGaji(objDokter.tunjangan, objDokter.gaji))
main()
