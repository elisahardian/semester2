"""
Head
|
42| | -> 57| | -> 23| | -> 51| | -> Null
buatlah program yang menggambarkan single linked list diatas

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
linked_list.print_list()
