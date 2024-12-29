# LAT 3
## LATIHAN MENERAPKAN STATIC PADA METHOD DAN ATRIBUT, TIDAK MENERAPKAN KONSTRUKTOR
#LATHIAN DOKTER

#membuat kelas
class Dokter:
    #tanpa konstruktor
    #membuat class variabel
    id = None #bisa juga tulis ini: str(input("masukkan id: "))
    nama = None
    gaji= None
    #membuat method static dengan fungsi beserta parameter
    #method tunjangan
    @staticmethod
    def tunjangan(gaji):
        return 0.1 * gaji
    @staticmethod
    def totalGaji(gaji):
        return 0.1 * gaji + gaji

#program utama
def main():
    Dokter.id = str(input("masukkan id\t: "))
    Dokter.nama = str(input("Masukkan nama\t: "))
    Dokter.gaji = int(input("Masukkan gaji\t: "))
    print("tunjangan\t: ", Dokter.tunjangan(Dokter.gaji))
    print("total gaji\t: ", Dokter.totalGaji(Dokter.gaji))
main()