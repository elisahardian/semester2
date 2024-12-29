
#membuat kelas
class Nilai:
    #membuat konstruktor
    def __init__ (self, uts, tugas, uas):
        self.uts=uts
        self.tugas=tugas
        self.uas=uas
    #membuat method dengan fungsi
    def totalnilai(self):
        total_nilai = (0.3 * self.uts) + (0.2 * self.tugas) + (0.5 * self.uas)
        return total_nilai
    #membuat method dengan fungsi
    def grade(self):
        total_nilai = self.totalnilai()
        if total_nilai >= 80:
            return "A"
        elif total_nilai >= 60:
            return "B"
        elif total_nilai >= 40:
            return "C"
        elif total_nilai >= 20:
            return "D"
        else:
            return "E"
#blok main program
def main():
    #instansiasi kelas menjadi objek 
    objNilai = Nilai(None, None, None)
    objNilai.uts=int(input("masukkan nilai uts\t: "))
    objNilai.tugas=int(input("masukkan tugas\t: "))
    objNilai.uas=int(input("masukkan nilai uas\t: "))
    print(objNilai.grade())            
main()

