# PEMBUNGKUSAN DENGAN INTERFACE

#import zope
import zope.interface 

#membuat interface
class InfDokter(zope.interface.Interface):
    def tunjangan(self):
        pass
    def hitung_total(self):
        pass

#mengimplementasikan interface di kelas konkret
@zope.interface.implementer(InfDokter)
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji

    #method tunjangan
    def tunjangan(self):
        return self.gaji * 0.1

    #method total 
    def hitung_total(self):
        return self.gaji + self.tunjangan()

#main program
def main():
    #instansiasi kelas menjadi objek
    objDokter = Dokter(None, None, None)

    print("-"*40)
    print("<<MASUKKAN DATA>>")
    print("-"*40)
    objDokter.id = str(input("masukkan id dokter: "))
    objDokter.nama = str(input("masukkan nama dokter: "))
    objDokter.gaji = int(input("masukkan gaji: "))
    print("-"*40)
    print("id dokter: ", objDokter.id)
    print("nama dokter: ", objDokter.nama)
    print("gaji: ", '{:0,.2f}'.format(objDokter.gaji))
    print("tunjangan: ", '{:0,.2f}'.format(objDokter.tunjangan()))
    print("total gaji: ", '{:0,.2f}'.format(objDokter.hitung_total()))
main()    

