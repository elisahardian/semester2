## SINGLE INHERITANCE. PUBLIC

#membuat kelas induk
class Dokter:
    #membuat konstruktor
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji
    #method tunjangan
    def tunjangan(self):
        return self.gaji * 0.1
    
#membuat kelas turunan
class DokSpesialis(Dokter):
    #memuat konstruktor
    def __init__(self, id, nama, gaji, tunspesialis):
        super().__init__(id, nama, gaji)
        self.tunspesialis = tunspesialis
    #bila tanpa parameter
    def uang_makan(self):
        return self.gaji * 0.1
    #method  total
    def hitung_total(self):
        return self.gaji + self.tunjangan() + self.tunspesialis + self.uang_makan()  

#main program
def main():
    #instansiasi kelas menjadi objek
    objDokterS= DokSpesialis (None, None, None, None)

    objDokterS.id = str(input("masukkan id dokter\t: "))
    objDokterS.nama = str(input("masukkan nama dokter\t: "))
    objDokterS.gaji = int(input("masukkan gaji\t\t: "))
    #print("tunjangan\t\t: %.2f\n"+ objDokterS.uang_makan())
    #print("total gaji\t\t: %.2f\n"+ objDokterS.hitung_total())
    print("tunjangan\t\t: ", '{:0,.2f}'.format(objDokterS.tunjangan()))
    objDokterS.tunspesialis= int(input("masukkan tun.spesialis\t: "))
    #memanggil method uang makan tanpa parameter
    print("uang makan\t\t: ",'{:0,.2f}'.format(objDokterS.uang_makan()))
    print("total gaji\t\t: ", '{:0,.2f}'.format(objDokterS.hitung_total()))
main()