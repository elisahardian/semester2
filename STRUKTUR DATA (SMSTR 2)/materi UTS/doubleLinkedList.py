## CONTOH PROGRAM DOUBLE LINKEDLIST

class Simpul:
    def __init__(self, dat):
        self.dat = dat
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    def append(self, simpulBaru):
        ptr = self.head
        if ptr:
            while ptr.next:
                ptr = ptr.next
            ptr.next = simpulBaru
            simpulBaru.prev = ptr
        else:
            self.head = simpulBaru
    def sisip(self, setelah, simpulBaru):
        ptr = self.head
        while ptr and (ptr.dat != setelah):
            ptr = ptr.next
        if ptr.dat == setelah:
            simpulBaru.next = ptr.next
            simpulBaru.prev = ptr
            ptr.next = simpulBaru
    def hapus(self, dihapus):
        ptr = self.head
        while ptr and (ptr.dat != dihapus):
            ptr = ptr.next
        if ptr.dat == dihapus:
            if ptr.prev:
                ptr.prev.next = ptr.next
            else:
                self.head = ptr.next
            if ptr.next:
                ptr.next.prev = ptr.prev
            del ptr
    def cetak(self):
        print("HEAD <->", end=" ")
        #print("head: ", self.head)
        ptr = self.head
        while ptr:
            print(ptr.dat, end = " <-> ")
            #print("node: [", ptr.prev, "|", ptr.dat, "|", ptr.next, "]") #ptr.prev untuk menampilkan data sebelumnya. ptr.next menampilan alamat data sesudahnya
            ptr = ptr.next
        print("NULL")
a= [34, 77, 91, 23, 10, 32, 90, 60, 50, 11]
print("mulai")
l1=LinkedList()
l2=LinkedList()
l3=LinkedList()
for i in range(0, 10):
    temp = Simpul(a[i])
    l1.append(temp)
l1.sisip(10, Simpul(48))
l1.cetak()
print("ok")
xptr = l1.head
print(xptr)
while xptr:
    temp = Simpul(xptr.dat)
    if (xptr.dat %2 == 0):
        l2.append(temp)
    else:
        l3.append(temp)
    xptr = xptr.next
print("data genap")
l2.cetak()
print("data ganjil")
l3.cetak()
print("setelah hapus 10")
l1.hapus(10)
l1.cetak()
print("setelah hapus head")
l1.hapus(34)
print(l1.head)
l1.cetak()
print("setelah hapus tail")
l1.hapus(11)
l1.cetak()
