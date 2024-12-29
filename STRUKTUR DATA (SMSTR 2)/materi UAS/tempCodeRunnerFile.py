# QUEUE ARRAY BASED

SIZE = 10
queue = [-1] * SIZE
front = -1
rear = -1

def enQueue(value):
    global front, rear
    if rear == SIZE - 1:
        print("\nAntrian sudah penuh, tidak bisa enqueue.")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = value
        print("\nData berhasil ditambahkan.")

def deQueue():
    global front, rear
    if front == rear:
        print("\nAntrian kosong, tidak bisa dequeue.")
    else:
        print("\nData yang keluar:", queue[front])
        front += 1
        if front == rear:
            front = rear = -1

def display():
    if rear == -1:
        print("\nAntrian kosong")
    else:
        print("\nData dalam antrian adalah:")
        for i in range(front, rear + 1):
            print(queue[i], end="\t")

while True:
    print("\n\n*** MENU ***\n")
    print("1. Enqueue\n2. Dequeue\n3. Tampilkan Data\n4. Selesai")
    choice = int(input("pilih: "))
    if choice == 1:
        value = int(input("ketik angka yang akan enqueue: "))
        enQueue(value)
    elif choice == 2:
        deQueue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("\nCoba lagi ya!!!")