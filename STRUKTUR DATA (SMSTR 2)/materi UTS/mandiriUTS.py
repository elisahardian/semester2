"""
# record pada python
#define class
class beverage:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
#membuat objek tunggal dari class beverage
p1 = beverage("bajigur", 25000)
#membuat array objek dari class beverage
p = []
p.append(beverage("bajigur", 25000))
p.append(beverage("es doger", 15000))
p.append(beverage("puding", 5000))
p.append(beverage("cendol", 10000))
#cara mengakses
print(p1.nama, p1.harga)
print(p[0].nama, p[0].harga)
print(p[1].nama, p[1].harga)
print(p[2].nama, p[2].harga)
print(p[3].nama, p[3].harga)
"""
"""
#array
m=[[1,2,3], [4,5,6], [7,8,9]]
print(m)
print(m[0])
print(m[2])
print(m[0][0], m[0][1], m[0][2])
print(m[1][0], m[1][1], m[1][2])
for i in m:
    print(i)
for i in m:
    for j in i:
        print(j)
for i in range(0, 3):
    for j in range(0, 3):
        if j < 2:
            print(m[i][j], end=" ")
        else:
            print(m[i][j])

m=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(m)
print(m[0])
print(m[1])
print("panjang: ", len(m))
for i in range(0, 9):
    print(m[i], end=" ")
print()
for i in m:
    print(i)
m.append(10)
for i in range(0, 10):
    print(m[i], end=" ")
print("panjang: ", len(m))
m.pop(9)
for i in range(0, len(m)):
    print(m[i], end=" ")
print("panjang: ", len(m))
m.pop(5)
for i in range(0, len(m)):
    print(m[i], end = " ")
print("panjang: ", len(m))
print()
m.insert(5, 100)
print(m)
m[3] = 999
print(m)
m.sort()
print(m)
m.reverse()
print(m)
m.remove(2)
print(m)
n = [111, 112, 113]
m.extend(n)
print(m)
m.clear()
print(m)
"""
"""
#pembutan kelas dan objek
#mendefinisikan kelas
class Kendaraan:
    def __init__(self, jenis, roda):
        self.jenis = jenis
        self.roda = roda
    def info(self):
        print(f"jenis: {self.jenis}, roda: {self.roda}")
#membuat objek dari kelas kendaraan
mobil = Kendaraan(jenis="mobil", roda=4)
sepeda =Kendaraan(jenis="sepeda", roda=2)
#mengakses atribut dan method objek
print(mobil.jenis)
sepeda.info()
"""
"""
#pembuatan single linked list view all and add first
class SingleLL:
    #pembuatan kelas node
    class _Node:
        def __init__(self, element, nextNode=None):
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
    #add first pada ll yang maih kosong
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1
    def __len__(self):
        return self._size
def main():
    mylist = SingleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print(str(mylist))
    print(len(mylist))
main()
"""
"""
#contoh insert ditengah

#pembuatan single linked list view all and add first
class SingleLL:
    #pembuatan kelas node
    class _Node:
        def __init__(self, element, nextNode=None):
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
    #add first pada ll yang maih kosong
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
    mylist = SingleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print("awal")
    print(str(mylist))
    print(len(mylist))
    #menambahkan node
    mylist.add_middle(2, 20)
    print("setelah")
    print(str(mylist))
    print(len(mylist))
main()
"""
"""
#delete pada akhir list
class SingleLL:
    #pembuatan kelas node
    class _Node:
        def __init__(self, element, nextNode=None):
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
    #add first pada ll yang maih kosong
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1
    #menghapus node diakhir linked list
    def delete_last(self):
        if self._head is None:
            raise IndexError("linked list os empty")
        elif self._size == 1:
            self._head = None
        else:
            current_node = self._head
            while current_node.nextNode.nextNode is not None:
                current_node = current_node.nextNode
            current_node.nextNode = None
        self._size -=1
    def __len__(self):
        return self._size
def main():
    mylist = SingleLL()
    mylist.add_first(50)
    mylist.add_first(30)
    mylist.add_first(10)
    print("awal: ")
    print(str(mylist))
    print(len(mylist))
    #menghapus node
    mylist.delete_last()
    print("setelah delete last: ")
    print(str(mylist))
    print(len(mylist))
main()
"""