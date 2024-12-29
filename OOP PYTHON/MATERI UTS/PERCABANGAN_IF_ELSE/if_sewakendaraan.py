# PROGRAM MENGHITUNG SEWA KENDARAAN ( DARI JAVA KE PYTHON )

#membuat kelas
class sewakendaraan:
    #membuat konstruktor
    def __init__ (self, __idpenyewa, __nama, __alamat, __noktp, __notelepon, __jeniskendaraan, __noplat, __lamasewa, __biayasewa ):
        self.__idpenyewa=__idpenyewa
        self.__nama=__nama
        self.__alamat=__alamat
        self.__noktp=__noktp
        self.__notelepon=__notelepon
        self.__jeniskendaraan=__jeniskendaraan
        self.__noplat=__noplat
        self.__lamasewa=__lamasewa
        self.__biayasewa=__biayasewa
    #menerapkan property method 
    def setIdpenyewa(self, __idpenyewa):
        self.__idpenyewa = __idpenyewa
    def getIdpenyewa(self):
        return self.__idpenyewa
    def setNama(self, __nama):
        self.__nama = __nama
    def getNama(self):
        return self.__nama
    def setAlamat(self, __alamat):
        self.__alamat = __alamat
    def getAlamat(self):
        return self.__alamat
    def setNoktp(self, __noktp):
        self.__noktp = __noktp
    def getNoktp(self):
        return self.__noktp
    def setNotelepon(self, __notelepon):
        self.__notelepon = __notelepon
    def getNotelepon(self):
        return self.__notelepon
    def setJeniskendaraan(self, __jeniskendaraan):
        self.__jeniskendaraan = __jeniskendaraan
    def getJeniskendaraan(self):
        return self.__jeniskendaraan
    def setNoplat(self, __noplat):
        self.__noplat = __noplat
    def getNoplat(self):
        return self.__noplat
    def setLamasewa(self, __lamasewa):
        self.__lamasewa = __lamasewa
    def getLamasewa(self):
        return self.__lamasewa
    def setBiayasewa(self, __biayasewa):
        self.__biayasewa = __biayasewa
    def getBiayasewa(self):
        return self.__biayasewa

    #membuat method dengan fungsi. total sewa
    def totalsewa(self):
        return self.__lamasewa * self.__biayasewa
    #membuat method dengan fungsi. potongan harga
    def potonganharga(self):
        if self.__lamasewa >= 7:
            return 0.05 * self.totalsewa()
        elif self.__lamasewa >= 5:
            return 0.03 * self.totalsewa()
        elif self.__lamasewa >= 3:
            return 0.02 * self.totalsewa()
        else:
            return 0
    #membuat method dengan fungsi. ppn
    def ppn(self):
        return 0.02 * self.totalsewa()
    #membuat method dengan fungsi. jumlah bayar
    def jumlahbayar(self):
        return self.totalsewa() - self.potonganharga() + self.ppn()

#blok main program
def main():
    #instansiasi kelas menjadi objek 
    objSewakendaraan = sewakendaraan(None, None, None, None, None, None, None, None, None)
    objSewakendaraan.setIdpenyewa(str(input("ID penyewa\t: ")))
    objSewakendaraan.setNama(str(input("Nama\t: ")))
    objSewakendaraan.setAlamat(str(input("Alamat\t: ")))
    objSewakendaraan.setNoktp(str(input("No KTP\t: ")))
    objSewakendaraan.setNotelepon(str(input("No telepon\t: ")))
    objSewakendaraan.setJeniskendaraan(str(input("Jenis kendaraan\t: ")))
    objSewakendaraan.setNoplat(str(input("No plat\t: ")))
    objSewakendaraan.setLamasewa(int(input("Lama sewa\t: ")))
    objSewakendaraan.setBiayasewa(int(input("Biaya sewa\t: ")))
    print("Total sewa\t: ", objSewakendaraan.totalsewa())
    print("Potongan harga\t: ", objSewakendaraan.potonganharga()) 
    print("PPN\t: ", objSewakendaraan.ppn())
    print("Jumlah bayar\t: ", objSewakendaraan.jumlahbayar())     
main()
