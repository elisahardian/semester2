"""
class Simpul:
    def __init__(self):
        self.dat = ""   # Data dalam simpul, diinisialisasi sebagai string kosong
        self.next = None  # Pointer ke simpul berikutnya, diinisialisasi sebagai None

# Fungsi untuk membuat linked list
def buat_linked_list():
    temp = None  # Deklarasi variabel temp untuk menyimpan simpul sementara
    head = None  # Inisialisasi kepala linked list
    ptr = None   # Inisialisasi pointer untuk traversal

    # Program Utama
    while True:
        masukan = int(input("Input Data: "))   # Meminta input dari pengguna
        
        if len(masukan) > 0:
            # Menggunakan slicing untuk memastikan panjang data tidak melebihi 10 karakter
            masukan = masukan[:10].ljust(10)

            masukan=int(input("berapa panjang: "))

            # Tentukan alokasi memori baru untuk simpul
            temp = Simpul()

            # Isi data ke dalam simpul
            temp.dat = masukan
            temp.next = None

            # Periksa apakah linked list kosong
            if head is None:
                # Tentukan kepala linked list
                head = temp
                ptr = head
            else:
                # Sambungkan link ptr terakhir ke link baru
                ptr.next = temp
                ptr = ptr.next
        else:
            break   # Keluar dari loop jika panjang data kurang dari atau sama dengan 0

    print()

    # Tampilkan semua simpul dalam linked list
    if head is not None:
        ptr = head
        print("cell: {Alamat} [ Data | Cell berikut]")

        while ptr is not None:
            # Tampilkan informasi alamat, data, dan alamat simpul berikutnya
            print(f"cell: {{ {hex(id(ptr))} }} [ {ptr.dat} | {hex(id(ptr.next))} ]")
            ptr = ptr.next

# Panggil fungsi untuk membuat linked list
buat_linked_list()
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
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
        print("head -> ", end="")
        while temp is not None:
            print(temp.data, end="")
            if temp.next is not None:
                print(" -> ", end="")
            else:
                print(" -> None", end="")
            temp = temp.next
        print()

# Main function
if __name__ == "__main__":
    # Creating linked list object
    my_list = LinkedList()

    # Adding some nodes to the linked list
    my_list.append(42)
    my_list.append(57)
    my_list.append(23)
    my_list.append(51)

    # Displaying the contents of the linked list
    my_list.display()
