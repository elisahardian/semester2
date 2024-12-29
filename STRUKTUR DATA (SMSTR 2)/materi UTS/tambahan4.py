"""
kemudian pada kodingan diatas buatlah program untuk
1. Menambahkan node baru 10 setelah node 51
2. sisipkan node baru 10 sebelum node 51
3. Hapus node 23 dari single linked list
"""

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
            print("Node tidak ditemukan dalam linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, next_node, data):
        if self.head is None:
            print("Linked list kosong")
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
        print("Node tidak ditemukan dalam linked list")

    def delete_node(self, data):
        if self.head is None:
            print("Linked list kosong")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("Node tidak ditemukan dalam linked list")

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} ->", end=" ")
            current = current.next
        print("Null")

# Membuat instance LinkedList
linked_list = LinkedList()

# Menambahkan node
linked_list.append(42)
linked_list.append(57)
linked_list.append(23)
linked_list.append(51)

# Menampilkan linked list
print("Linked List Awal:")
linked_list.print_list()

# Menambahkan node 10 setelah node 51
linked_list.insert_after(linked_list.head.next.next.next, 10)

# Menyisipkan node 10 sebelum node 51
linked_list.insert_before(linked_list.head.next.next.next, 10)

# Menghapus node 23
linked_list.delete_node(23)

# Menampilkan linked list setelah modifikasi
print("\nLinked List Setelah Modifikasi:")
linked_list.print_list()

