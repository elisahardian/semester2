"""
## PROGRAM PEMBUATAN KELAS DAN OBJEK
#mendefinisikan kelas
class Kendaraan:
    def __init__(self, jenis, roda):
        self.jenis = jenis
        self.roda = roda
    def info(self):
        print(f"jenis: {self.jenis}, roda: {self.roda}")
#membuat objek dari kelas Kendaraan
mobil = Kendaraan(jenis="mobil", roda=4)
sepeda = Kendaraan(jenis="sepeda", roda=2)
#mengakses atribut dan method objek
print(mobil.jenis)
print(mobil.roda)
sepeda.info()
"""

## CONTOH PEMBUATAN SINGLE LINKED LIST
"""
#pembuatan struktur single linkedlist dan node
class singleLL:
    #pembuatan kelas node
    class _Node:
        def __init__ (self, element, nextNode = None):
            self.element = element
            self.nextNode = nextNode
    #pembuatan single linked list
    def __init__(self):
        self.head = None
        self._size = 0
"""
"""
##pembuatan single linkedlist view all & add first
#pembuatan struktur linkedlist dan node
class singleLL:
    #pembuatan kelas node
    class _Node:
        def __init__ (self, element, nextNode = None):
            self.element = element
            self.nextNode = nextNode
    #pembuatan single linked list
    def __init__(self):
        self._head = None
        self._size = 0 
    #pembuatan fungsi view all
    def __str__(self):
        result = " "
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result
    #add first pada list yang masih kosong
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1
    def __len__(self):
        return self._size

def main():
    mylist = singleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print(str(mylist))
    print(len(mylist))
main()

print("=="*10)
"""

"""
## CONTOH INSERT DITENGAH
class singleLL:
    #pembuatan kelas node
    class _Node:
        def __init__ (self, element, nextNode = None):
            self.element = element
            self.nextNode = nextNode
    #pembuatan single linked list
    def __init__(self):
        self._head = None
        self._size = 0 
    #pembuatan fungsi view all
    def __str__(self):
        result = " "
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result
    #add first pada list yang masih kosong
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1
    #menambahkan node ditengah linkedlist
    def add_middle(self, index, element):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.add_first(element)
        else:
            newNode = self._Node(element)
            current_node = self._head
            for _ in range(index - 1):
                current_node = current_node.nextNode
                newNode.nextNode = current_node.nextNode
                current_node.nextNode = newNode
                self._size += 1
    def __len__(self):
        return self._size
def main():
    mylist = singleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print("original linked list: ")
    print(str(mylist))
    print(len(mylist))

    #menambahkan node ditengah (index 1)
    mylist.add_middle(1, 20) # kalo diindex ke 1 gamau, diindex 0 atau 2 mau
    print("linked list setelah menambahkan node ditengah: ")
    print(str(mylist))
    print(len(mylist))
main()
"""    

## DELETE PADA AKHIR LIST

class singleLL:
    #pembuatan kelas node
    class _Node:
        def __init__ (self, element, nextNode = None):
            self.element = element
            self.nextNode = nextNode
    #pembuatan single linked list
    def __init__(self):
        self._head = None
        self._size = 0 
    #pembuatan fungsi view all
    def __str__(self):
        result = " "
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result
    #add first pada list yang masih kosong
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1
    #menghapus mode diakhir linked list
    def delete_last(self):
        if self._head is None:
            raise IndexError("linked list is empty")
        elif self._size == 1:
            self._head = None
        else:
            current_node = self._head
            while current_node.nextNode.nextNode is not None:
                current_node = current_node.nextNode
            current_node.nextNode = None
        self._size -= 1
    def __len__(self):
        return self._size
def main():
    mylist = singleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print("original linked list: ")
    print(str(mylist))
    print(len(mylist))
    
    #menghapus node diakhir
    mylist.delete_last()
    print("linked list setelah menghapus node diakhir: ")
    print(str(mylist))
    print(len(mylist))
main()

print()
## MENUKARKAN POSISI SINGLE LINKED LIST BERDASARKAN INPUTAN USER
array = [42, 57, 23, 51]
print("list saat ini: ", array)
a = int(input("index elemen pertama yang ingin ditukar: "))
b = int(input("index elemen kedua yang ingin ditukar: "))
def tukar(array):
    array[a], array[b] = array[b], array[a]
    return array
print(tukar(array))
