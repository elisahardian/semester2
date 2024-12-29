
## CONTOH VARIABEL POINTER
import ctypes
a = 10
print("alamat variabel a dalam desimal: ", id(a))
print("alamat variabel a dalam hexadesimal: ", hex(id(a)))
alamat = id(a)
dat = ctypes.cast(alamat, ctypes.py_object).value
print("isi alamat [{}] adalah {}".format(hex(alamat), dat))


"""
## POINTER PYTHON
class Simpul:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
        self.next = None
class LinkedList():
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
    temp = Simpul(a[i]) #GA BISA JALAN KARENA a NYA GA ADA
    ll.append(temp)
"""

