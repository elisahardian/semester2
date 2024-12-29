## KELAS ABSTRAK

#import library ABC
from abc import ABC, abstractmethod

#membuat kelas abstrak
class abstrak_pegawai(ABC):
    #membuat method abstrack
    @abstractmethod
    def tunjangan(self):
        pass

    @abstractmethod
    def bonus(self):
        pass

    @abstractmethod
    def total(self):
        pass

#membuat kelas konkrit
class pegawai(abstrak_pegawai):
    #membuat konstruktor
    def __init__(self, __id, __nama, __gaji):
        self.__id = __id
        self.__nama = __nama
        self.__gaji = __gaji
    #menerapkan set dan get
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
    
    #overriding method abstrack
    def tunjangan(self):
        return self.__gaji * 0.1
    def bonus(self):
        return self.__gaji * 0.15
    def total(self):
        return self.__gaji + self.tunjangan() + self.bonus()

#program utama
def main():
    #instansiasi kelas menjadi objek
    objPegawai = pegawai (None, None, None)

    print("-"*45)
    print("<<MASUKKAN IDENTITAS PEGAWAI>>")
    print("-"*45)
    objPegawai.setId(input("masukkan id: "))
    objPegawai.setNama(input("masukkan nama: "))
    objPegawai.setGaji(int(input("masukkan gaji: ")))
    print("-"*45)
    print("<<DATA PEGAWAI>>")
    print("-"*45)
    print("ID pegawai: ", objPegawai.getId())
    print("nama pegawai: ", objPegawai.getNama())
    print("gaji pegawai: ",'{:0,.2f}'.format(objPegawai.getGaji()))
    print("tunjangan: ", '{:0,.2f}'.format(objPegawai.tunjangan()))
    print("bonus: ", '{:0,.2f}'.format(objPegawai.bonus()))
    print("total: ", '{:0,.2f}'.format(objPegawai.total()))
main()