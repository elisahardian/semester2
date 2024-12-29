"""
#menukarkan posisi single linked list berdasarkan inputan user
array = [42, 57, 23, 51]
print("list saat ini:", array)
a= int(input("index pertama yg mau ditukar: "))
b= int(input("index kedua yg mau ditukar: "))
def tukar(array):
    array[a], array[b] = array[b], array[a]
    return array
print(tukar(array))
"""
"""
#contoh codingan single linked list python lengkap
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
        print("HEAD", end=" -> ")
        ptr = self.head
        while ptr:
            print(ptr.dat, end=" -> ")
            ptr = ptr.next
        print("NULL")

a=[34, 77, 91, 23, 10, 32, 90, 60, 50 ,11]
l1 = LinkedList()
for i in range(0, 10):
    temp = Simpul(a[i])
    l1.append(temp)
l1.sisip(10, Simpul(48))
l1.cetak()
l1.hapus(10)
print("setelah hapus 10")
l1.cetak()
l1.hapus(34)
print("setelah hapus head")
l1.cetak()
l1.hapus(11)
print("setelah hapus tail")
l1.cetak()
"""


## MEMBUAT SINGLE LL. HEAD 42 57 23 51 NULL
#cara 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        print("head -> ", end = "")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")
#membuat linkedlist
llist=LinkedList()
data_list=[42, 57, 23, 51]
for data in data_list:
    llist.insert(data)
#menampilkan linkedlist
llist.display() 
#cara2
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        print("head -> ", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            if temp.next is not None:
                print("->", end=" ")
            else:
                print("-> null", end=" ")
            temp = temp.next
        print()
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(42)
    my_list.append(57)
    my_list.append(23)
    my_list.append(51)
    my_list.display()
#cara 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def print_list(self):
        print("head ->", end=" ")
        current = self.head
        while current:
            print(f"{current.data}->", end=" ")
            current = current.next
        print("null")
linked_list= LinkedList()
linked_list.append(42)
linked_list.append(57)
linked_list.append(23)
linked_list.append(51)
linked_list.print_list()

