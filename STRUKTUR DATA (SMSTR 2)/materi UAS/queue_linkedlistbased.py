class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        val = int(input("Menambahkan data kedalam queue: "))
        new_node = Node(val)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Antrian kosong, tidak bisa dequeue")
            return
        else:
            print("Data yang keluar:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None and self.rear is None:
            print("Antrian kosong.")
            return
        print("Data dalam antrian adalah:", end=" ")
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def main():
    queue = Queue()
    done = False
    while not done:
        print("\n1) Enqueue")
        print("2) Dequeue")
        print("3) Tampilkan data antrian")
        print("4) Selesai")
        choice = int(input("Pilih: "))
        if choice == 1:
            queue.enqueue()
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Keluar")
            done = True
        else:
            print("Coba lagi ya!!!")

if __name__ == "__main__":
    main()