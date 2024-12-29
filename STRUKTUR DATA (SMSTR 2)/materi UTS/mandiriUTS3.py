## mmodifikssi single ll
#cara 1
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
        print("head", end="->")
        ptr = self.head
        while ptr:
            print(ptr.dat, end="->")
            ptr = ptr.next
        print("none")
a=[42, 57, 23, 51]
ll=LinkedList()
for i in range(0, 4):
    temp = Simpul(a[i])
    ll.append(temp)
ll.cetak
print("sisip angka 10 setelah angka 51")
ll.sisip(51, Simpul(10))
ll.cetak()
print("sisip angka 10, setelah angka 23 / sisip sebelum angka 51")
ll.sisip(23, Simpul(10))
ll.cetak()
print("setelah hapus 23")
ll.hapus(23)
ll.cetak()

print("\n")
#cara 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
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
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("node tidak ditemukan dalam linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insert_before(self, next_node, data):
        if self.head is None:
            print("linked list kosong")
            return 
        if self.head.data == next_node.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.data == next_node.data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("node tidak ditemukan dalam linked list")
    def delete_node(self, data):
        if self.head is None:
            print("linked list kosong")
            return
        if self.head.data == data:
            self.head = self.head.next
            return 
        current = self.head
        while current.next :
            if current.next.data == data:
                current.next = current.next.next
                return 
            current = current.next
        print("node tidak ditemukan dalam linkde list")
    def print_list(self):
        print("head ->", end="")
        current = self.head
        while current:
            print(f"{current.data}->", end = "")
            current = current.next
        print("none")
#membuat instance linked list
ll= LinkedList()
#menambahka node
ll.append(42)
ll.append(57)
ll.append(23)
ll.append(51)
#menampilkan linkedlist
print("linkdelist awal:")
ll.print_list()
#menambhakan node 10 setelah node 51
ll.insert_after(ll.head.next.next.next, 10)
#menyisipkan node 10 sebelum node 51
ll.insert_before(ll.head.next.next.next, 10)
#menghapus node 23
ll.delete_node(23)
#menampilkan ll setelah dimodifikasi
print("linked list setelah dimodifikasi")
ll.print_list()
