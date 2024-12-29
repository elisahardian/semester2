## POLYMORPHISM DENGAN PEWARISAN OVERRIDING

#membuat kelas induk pegawai
class Pegawai:
    #membuat konstruktor
    def __init__(self, id, nama, gaji, status):
        self.id = id
        self.nama = nama
        self.gaji = gaji
        self.status = status
    #method hitung
    def hitung(self):
        return self.gaji * 0.02

#membuat kelas tetap 
class Tetap(Pegawai):
    #method hitung untuk override hitung dikelas induk
    def hitung(self, gaji):
        self.gaji = gaji
        return self.gaji * 0.1
    #method total
    def total(self, gaji):
        self.gaji = gaji
        return self.gaji + self.hitung(self.gaji)

#membuat kelas kontrak
class Kontrak(Pegawai):
    #method hitung untuk override hitung di kelas induk
    def hitung(self, gaji):
        self.gaji = gaji
        return self.gaji * 0.05
    #method total
    def total(self, gaji):
        self.gaji = gaji
        return self.gaji + self.hitung(self.gaji)

#main program
def main():
    jawab = 'y'
    while jawab =='y':
        #instansiasi kelas menjadi objek
        objPegawai = Pegawai (None, None, None, None)
        print("-"*40)
        print("<<MASUKKAN DATA>>")
        print("-"*40)
        objPegawai.id = str(input("Masukkan id dokter: "))
        objPegawai.nama = str(input("masukkan nama: "))
        objPegawai.gaji = int(input("masukkan gaji: "))
        objPegawai.status = str(input("status [k/t]: "))
        print("-"*40)
        print("tunjangan lama (2%): ", '{:0,.2f}'.format(objPegawai.hitung()))
        if (objPegawai.status =='t'.lower()):
            #instansiasi kelas menjadi objek
            objTetap = Tetap(None, None, None, None)
            print("tunjangan baru (10%): ", '{:0,.2f}'.format(objTetap.hitung(objPegawai.gaji)))
            print("total gaji: ", '{:0,.2f}'.format(objTetap.total(objPegawai.gaji)))
        else:
            #instansiasi kelas menjadi objek
            objKontrak = Kontrak(None, None, None, None)
            print("tunjangan baru (5%): ", '{:0,.2f}'.format(objKontrak.hitung(objPegawai.gaji)))
            print("total gaji: ", '{:0,.2f}'.format(objKontrak.total(objPegawai.gaji)))
            print("-"*40)
        jawab = str(input("mau coba lagi [y/t]: ").lower())
main()