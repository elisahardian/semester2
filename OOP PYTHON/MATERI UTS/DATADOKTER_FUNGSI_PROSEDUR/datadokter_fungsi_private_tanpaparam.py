## PROGRAM MEMBUAT DATA DOKTER. DENGAN FUNGSI, TANPA PARAMETER, PRIVATE
#membuat kelas
class Dokter:
    #membuat konstruktor
    def __init__(self, __id, __nama, __gaji):
        self.__id = __id
        self.__nama = __nama
        self.__gaji = __gaji
    #menerapkan property method dengan set dan get
    def setId(self, __id):
        self.__id = __id
    def getId(self):
        return self.__id
    def setNama(self, __nama):
        self.__nama = __nama
    def getNama(self):
        return self.__nama
    def setGaji(self, __gaji):
        self.__gaji = __gaji
    def getGaji(self):
        return self.__gaji
    #membuat method dengan fungsi tanpa parameter
    #metode tunjangan
    def tunjangan(self):
        return 0.1 * self.__gaji
    #method total gaji
    def totalGaji(self):
        return self.tunjangan() + self.__gaji
#program utama
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter(None, None, None)
    objDokter.setId(str(input("masukkan id\t: ")))
    objDokter.setNama(str(input("masukkan nama\t: ")))
    objDokter.setGaji(float(input("masukkan gaji\t: ")))
    print("Tunjangan\t: ", objDokter.tunjangan())
    print("Total Gaji\t: ", objDokter.totalGaji())
main()
