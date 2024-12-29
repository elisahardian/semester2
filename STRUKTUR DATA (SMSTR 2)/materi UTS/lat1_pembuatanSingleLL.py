## PEMBUATAN SINGLE LINKED LIST. DENGAN HEAD - 42 - 57 - 23 - 51 - NULL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
        print("Head -> ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Membuat linked list
llist = LinkedList()
data_list = [42, 57, 23, 51]
for data in data_list:
    llist.insert(data)

# Menampilkan linked list
llist.display()