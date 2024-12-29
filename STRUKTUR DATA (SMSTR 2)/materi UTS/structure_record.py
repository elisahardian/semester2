"""
##CONTOH STRUCTURE RECORD

#define class
class beverage:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
#membuat objek tunggal dari class beverage
p1 = beverage("bajigur", 25000) # objek tunggal
#cara mengakses atribut/ property objek dari class beverage
print(p1.nama, p1.harga)
#membuat array objek dari class beverage

p = []
p.append(beverage("bajigur", 25000))
p.append(beverage("es doger", 15000))
p.append(beverage("puding", 5000))
p.append(beverage("cendol", 10000))

#cara mengakses atribut/ property objek dari class beverage
print(p1.nama, p1.harga)

print(p[0].nama, p[0].harga)
print(p[1].nama, p[1].harga)
print(p[2].nama, p[2].harga)
print(p[3].nama, p[3].harga)
"""
"""
##CONTOH GENERALISASI DALAM BENTUL RECORD/STRUCT MENJADI SEL ARRAY
#define class
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
#membuat array objek dari class mahasiswa
p = [] # list objek (array objek)
p.append(Mahasiswa("Nobita", 3223001, 0))
p.append(Mahasiswa("Shizuka", 3223002, 100 ))

print(p[0].nama, p[0].nim, p[0].nilai)
print(p[1].nama, p[1].nim, p[1].nilai)
"""

""" kode gajalan

## CONTOH GENERALISASI DALAM BENTUK RECORD/ STRUCT MENJADI SIMPUL LINKED LIST UNTUK STACK
class Simpul:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
        self.next = None
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    def append(self, simpulBaru):
        ptr = self.head
        if ptr:
            while ptr.next:
                ptr = ptr.next
            ptr.next = simpulBaru
        else:
            self.head = simpulBaru
ll = LinkedList()
for i in range(0, 10):
    temp = Simpul(a[i]) # a not defined
    ll.append(temp)
"""
