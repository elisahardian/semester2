## SINGLE INHERITANCE PRIVATE

#membuat kelas induk
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.__id = id
        self.__nama = nama
        self.__gaji = gaji
    #menerapkan set dan get
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
    def setNama(self, nama):
        self.__nama = nama
    def getNama(self):
        return self.__nama
    def setGaji(self, gaji):
        self.__gaji = gaji
    def getGaji(self):
        return self.__gaji
    #method tunjangan
    def tunjangan(self):
        return self.__gaji *0.1
    
#membuat kelas turunan 
class DokSpesialis(Dokter):
    #membuat konstruktor
    def __init__(self, tunspesialis):
        self.__tunspesialis = tunspesialis
    #menerapkan set dan get
    def setTunSpesialis(self, tunspesialis):
        self.__tunspesialis = tunspesialis
    def getTunSpesialis(self):
        return self.__tunspesialis

    #bila ada parameter
    def uang_makan(self, gaji):
        return gaji * 0.1
    
    #method total
    def hitung_total(self):
        return self.getGaji() + self.tunjangan() + self.getTunSpesialis() + self.uang_makan(self.getGaji())

#main program
def main():
    #instansiasi kelas menjadi objek
    objDokterS = DokSpesialis(None)
    objDokterS.setId = str(input("masukkan id dokter: "))
    objDokterS.setNama = str(input("masukkan nama dokter: "))
    objDokterS.setGaji(int(input("masukkan gaji: ")))
    print("tunjangan: ", '{:0,.2f}'.format(objDokterS.tunjangan()))
    objDokterS.setTunSpesialis(int(input("masukkan tun spesialis: ")))
    print("uang makan: ",'{:0,.2f}'.format(objDokterS.uang_makan(objDokterS.getGaji())))
    print("total gaji: ", '{:0,.2f}'.format(objDokterS.hitung_total()))
main()