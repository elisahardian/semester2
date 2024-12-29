# PEMBUNGKUSAN DENGAN PROPERTY METHOD

#membuat class
class Pegawai:
    def __init__ (self, id, nama, status, gaji):
        self.__id = id
        self.__nama = nama
        self.__status = status
        self.__gaji = gaji
    
    def getid(self):
        return self.__id
    def setid(self, id):
        self.__id = id
    def getnama(self):
        return self.__nama
    def setnama(self, nama):
        self.__nama = nama
    def getstatus(self):
        return self.__status
    def setstatus(self, status):
        self.__status = status
    def getgaji(self):
        return self.__gaji
    def setgaji(self, gaji):
        if gaji > 0:
            self.__gaji = gaji
    def tunjangan(self):
        if self.getstatus()=="t":
            return self.getgaji() * 0.1
        else:
            return self.getgaji() * 0.05
    def total(self):
        return self.getgaji() + self.tunjangan()

#main program
def main():
    objPeg = Pegawai(None, None, None, None)

    objPeg.setid(str(input("masukkan id: ")))
    objPeg.setnama(str(input("masukkan nama: ")))
    objPeg.setstatus(str(input("status [T/K]: ").lower()))
    objPeg.setgaji(int(input("masukkan gaji: "))) 
    print("Tunjangan: ", objPeg.tunjangan())
    print("Total gaji: ", objPeg.total())   
main()