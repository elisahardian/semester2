## PROGRAM MODIFIKASI L=SINGLE LINKEDLIST. (PYTHON)
# HEAD -> 42 -> 57 -> 23 -> 51 -> NULL. DIMODIFIKASI. MENAMBAH NODE 10 SETELAH NODE 51. SISIPKAN NODE BARU 10 SEBELUM NODE 51. HAPUS NODE 23.

class Simpul:
    def __init__(self, dat):
        self.dat = dat
        self.next = None
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, simpulBaru):
        ptr = self.head
        if ptr:
            while ptr.next:
                ptr = ptr.next
            ptr.next = simpulBaru
        else:
            self.head = simpulBaru
    def sisip(self, setelah, simpulBaru):
        ptr = self.head
        while ptr and (ptr.dat != setelah):
            ptr = ptr.next
        if ptr.dat == setelah:
            simpulBaru.next = ptr.next
            ptr.next = simpulBaru
    def hapus(self, dihapus):
        ptr = self.head
        prev = None
        while ptr and (ptr.dat != dihapus):
            prev = ptr
            ptr = ptr.next
        if (ptr.dat == dihapus):
            if (prev == None):
                self.head = ptr.next
            else:
                prev.next = ptr.next
            del ptr
    def cetak(self):
        print("HEAD ->", end =" ")
        ptr = self.head
        while ptr:
            print(ptr.dat, end="->")
            ptr = ptr.next
        print("None")
a=[42, 57, 23, 51]
print("mulai")
l1=LinkedList()
for i in range(0, 4):
    temp = Simpul(a[i])
    l1.append(temp)
l1.cetak()
print("sisip angka 10, setelah angka 51")
l1.sisip(51, Simpul(10))
l1.cetak()
print("sisip angka 10, setelah angkak 57")
l1.sisip(57, Simpul(10))
l1.cetak()
print("setelah hapus angka 23")
l1.hapus(23)
l1.cetak()
