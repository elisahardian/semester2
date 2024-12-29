## POLYMORPHISM DENGAN OVERLOADING

#import library dispatch
from multipledispatch import dispatch

#membuat kelas induk pegawai
class Pegawai:
    #membuat konstruktor
    def __init__(self, id, nama, gaji, status):
        self.id = id
        self.nama = nama
        self.gaji = gaji
        self.status = status
    
    #method hitung untuk tunjangan
    @dispatch()
    def hitung(self):
        return self.gaji * 0.02
    #method hitung untuk tunjangan kontrak
    @dispatch(int) 
    def hitung(self, gaji):
        self.gaji = gaji 
        return self.gaji * 0.05
    #method hitung untuk tunjangan tetap
    @dispatch(int, str)
    def hitung(self, gaji, ket):
        self.gaji = gaji
        self.status = ket
        return self.gaji * 0.1
    #method total kontrak
    def total_k(self, gaji):
        self.gaji = gaji
        return self.gaji + self.hitung(self.gaji)
    #method total tetap
    def total_t(self, gaji):
        self.gaji = gaji
        return self.gaji + self.hitung(self.gaji, self.status) 

#main program
def main():
    jawab="y"
    while jawab =="y":
        #instansiasi kelas menjadi objek
        objPegawai = Pegawai (None, None, None, None)
        print("-"*40)
        print("<<MASUKKAN DATA>>")
        print("-"*40) 
        objPegawai.id = str(input("masukkan id pegawai: "))
        objPegawai.nama = str(input("masukkan nama pegawai: "))
        objPegawai.gaji = int(input("masukkan gaji: "))
        objPegawai.status = str(input("status [k/t]: ").lower())
        print("-"*40)
        print("tunjangan pegawai 2%: ", '{:0,.2f}'.format(objPegawai.hitung()))
        if (objPegawai.status =='k'):
            print("tunjangan kontrak 5%: ", '{:0,.2f}'.format(objPegawai.hitung(objPegawai.gaji)))
            print("status: ", objPegawai.status + " [-kontrak]")
            print("total gaji: ", '{:0,.2f}'.format(objPegawai.total_k(objPegawai.gaji)))
            print("-"*40)
        else:
            print("tunjangan tetap 10%: ", '{:0,.2f}'.format(objPegawai.hitung(objPegawai.gaji, objPegawai.status)))
            print("status: ", objPegawai.status + "[- tetap]")
            print("total gaji: ",'{:0,.2f}'.format(objPegawai.total_t(objPegawai.gaji)))
            print("-"*40)
        jawab = str(input("mau coba lagi[y/t]: ").lower())
main()
