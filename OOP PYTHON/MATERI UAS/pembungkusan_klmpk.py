# PEMBUNGKUSAN DENGAN PROPERTY METHOD
print("PROGRAM KEPEGAWAIAN \nBANK CENTRAL BUNDA MULIA")

#membuat class
class Pegawai:
    def __init__ (self, id, nama, notelp, status, gaji, alamat, gender, jamlembur, tagihan):
        self.__id = id
        self.__nama = nama
        self.__notelp = notelp
        self.__status = status
        self.__gaji = gaji
        self.__alamat = alamat
        self.__gender = gender
        self.__jamlembur = jamlembur
        self.__tagihan = tagihan
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    def getnama(self):
        return self.__nama
    def setnama(self, nama):
        self.__nama = nama
    def getnotelp(self):
        return self.__notelp
    def setnotelp(self, notelp):
        self.__notelp = notelp    
    def getstatus(self):
        return self.__status
    def setstatus(self, status):
        self.__status = status
    def getgaji(self):
        return self.__gaji
    def setgaji(self, gaji):
        if gaji > 0:
            self.__gaji = gaji
    def getalamat(self):
        return self.__alamat
    def setalamat(self, alamat):
        self.__alamat = alamat
    def getgender(self):
        return self.__gender
    def setgender(self, gender):
        self.__gender = gender
    def getjamlembur(self):
        return self.__jamlembur
    def setjamlembur(self, jamlembur):
        self.__jamlembur = jamlembur
    def gettagihan(self):
        return self.__tagihan
    def settagihan(self, tagihan):
        self.__tagihan = tagihan


    def tunjangan(self):
        if self.getstatus()=="t":
            return self.getgaji() * 0.1
        else:
            return self.getgaji() * 0.05
    def uangperawatan(self):
        if self.getgender()=="p":
            return self.getgaji() * 0.05
        else:
            return self.getgaji() * 0.03
    def uangmakan(self):
        return self.getgaji() * 0.1
    def uanglembur(self):
        if self.getjamlembur() >= 5:
            return (self.getgaji() * 0.15)
        elif self.getjamlembur() >=3:
            return (self.getgaji() * 0.1)
        elif self.getjamlembur() >=1:
            return (self.getgaji() * 0.05)
        else:
            return self.getgaji()
    def uangtagihan(self):
        return self.gettagihan()
    def total(self):
        return self.getgaji() + self.tunjangan() + self.uangperawatan() + self.uangmakan() + self.uanglembur() - self.uangtagihan()

#main program
def main():
    objPeg = Pegawai(None, None, None, None, None, None, None, None, None)

    objPeg.setid(str(input("masukkan id: ")))
    objPeg.setnama(str(input("masukkan nama: ")))
    objPeg.setnotelp(int(input("masukkan no telepon: ")))
    objPeg.setstatus(str(input("status [T/K]: ").lower()))
    objPeg.setgaji(int(input("masukkan gaji: "))) 
    objPeg.setalamat(str(input("masukkan alamat: ")))
    objPeg.setgender(str(input("masukkan gender [P/L]: ").lower()))
    objPeg.setjamlembur(int(input("masukkan berapa lama anda lembur dalam 1 minggu (dalam jam): ")))
    objPeg.settagihan(int(input("masukkan jumlah tagihan anda dalam 1 bulan: ")))

    print("Tunjangan: ", objPeg.tunjangan())
    print("Uang Perawatan: ", objPeg.uangperawatan())
    print("Uang Makan: ", objPeg.uangmakan())
    print("Bonus Lembur: ", objPeg.uanglembur())
    print("Uang Tagihan: ", objPeg.uangtagihan())
    print("Total gaji: ", objPeg.total())   
    print("Jadi gaji anda dalam bulan ini adalah ", objPeg.total())
main()