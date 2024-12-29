#MULTIARY TREE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        else:
            dequeue = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return dequeue
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        else:
            return self.front.data
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
"""
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print("queue setelah enqueue: ")
queue.display()
"""

queue = Queue()
while True:
    print("\nMenu:\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
    choice = input("pilih (1/2/3/4/5): ")
    if choice == "1":
        data = input("data yang ingin dimasukkan keantrian: ")
        queue.enqueue(data)
        print("data", data, "telah dimasukan kedalam antrian")
    elif choice == "2":
        removed_data = queue.dequeue()
        if removed_data is not None:
            print("data", removed_data, "telah dihapus dari antrian")
    elif choice == "3":
        front_data = queue.peek()
        if front_data is not None:
            print("elemen pertama dalam antrian: ", front_data)
    elif choice == "4":
        print("isi dari antrian: ")
        queue.display()
    elif choice == "5":
        print("program berhenti")
        break
    else:
        print("pilihan tidka valid. coba lagi")
        