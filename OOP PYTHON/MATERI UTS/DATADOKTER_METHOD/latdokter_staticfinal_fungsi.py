# LAT 5
## LATIHAN MENERAPKAN STATIC FINAL
#LATHIAN DOKTER. 
#karena ada FINAL = TIDAK BISA DIUBAH

#membuat kelas
class Dokter:
    #atribut "final" dengan konvensi
    ID = "ID123" #konvensi = nama atribut dalam huruf besar....
    NAMA = "Dokter ABC" #konvensi = nama atribut dalamm huruf besar...
    GAJI = 5000000 #konvensi = nama atribut dalamm huruf besar...
    @staticmethod
    def tunjangan(gaji):
        return 0.1 * gaji
    @staticmethod
    def totalGaji(gaji):
        return gaji + Dokter.tunjangan(gaji)
#main program
def main():
    print("ID\t: ", Dokter.ID)
    print("Nama\t: ", Dokter.NAMA)
    print("Gaji\t: ", Dokter.GAJI)
    print("Tunjangan\t: ", Dokter.tunjangan(Dokter.GAJI))
    print("Total Gaji\t: ", Dokter.totalGaji(Dokter.GAJI))
main()


