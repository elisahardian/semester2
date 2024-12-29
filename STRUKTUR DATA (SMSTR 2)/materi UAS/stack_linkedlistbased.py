"""
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("Popped element is:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            ptr = self.top
            print("Stack elements are:", end=" ")
            while ptr is not None:
                print(ptr.data, end=" ")
                ptr = ptr.next
            print()

stack = Stack()

while True:
    print("1) Push to stack")
    print("2) Pop from stack")
    print("3) Display stack")
    print("4) Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter the value to push: "))
        stack.push(value)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
"""
#bisa juga kalau gamau pake import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack kosong")
        else:
            print("Elemen yang di-pop adalah:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack kosong")
        else:
            ptr = self.top
            print("Elemen Stack adalah:", end=" ")
            while ptr is not None:
                print(ptr.data, end=" ")
                ptr = ptr.next
            print()

stack = Stack()
running = True

while running:
    print("1) Push ke stack")
    print("2) Pop dari stack")
    print("3) Tampilkan stack")
    print("4) Keluar")
    
    pilihan = int(input("pilih: "))
    
    if pilihan == 1:
        nilai = int(input("ketik nilai yang akan dipush: "))
        stack.push(nilai)
    elif pilihan == 2:
        stack.pop()
    elif pilihan == 3:
        stack.display()
    elif pilihan == 4:
        print("selesai")
        running = False
    else:
        print("salah pilih")
