## CONTOH KODINGAN SINGLEL LINKED LIST PYTHON

class Simpul:
    def __init__(self, dat):
        self.dat = dat
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
        print("HEAD ", end = "->")
        ptr = self.head
        while ptr:
            #print("node: ", ptr, "[", ptr.dat, "|", ptr.next, "]")
            print(ptr.dat, end = "->")
            ptr = ptr.next
        print("NULL")
a=[34, 77, 91, 23, 10, 32, 90, 60, 50, 11]
print("mulai")
l1= LinkedList()
l2= LinkedList()
l3= LinkedList()
for  i in range(0, 10):
    temp = Simpul(a[i])
    l1.append(temp)
l1.sisip(10, Simpul(48))
l1.cetak()
print("ok")
xptr = l1.head
print(xptr)
while xptr:
    temp = Simpul(xptr.dat)
    if (xptr.dat % 2 == 0):
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
l1.cetak()
print("setelah hapus tail")
l1.hapus(11)
l1.cetak()
