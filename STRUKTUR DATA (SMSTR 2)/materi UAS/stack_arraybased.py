#Contoh implementasi Stack Python menggunakan Array (ada menu)

stack = []
n = 100

def push(val):
    if len(stack) >= n:
        print("Stack sudah penuh")
    else:
        stack.append(val)

def pop():
    if not stack:
        print("Stack kosong")
    else:
        print("Elemen yang di pop =", stack.pop())

def display():
    if stack:
        print("Elemen stack adalah:", end=" ")
        for item in reversed(stack):
            print(item, end=" ")
        print()
    else:
        print("Stack kosong")

while True:
    print("1) Push ke Stack")
    print("2) Pop dari Stack")
    print("3) Tampilkan Stack")
    print("4) Selesai")
    ch = int(input("Pilih: "))
    
    if ch == 1:
        val = int(input("Ketik nilai yang akan di push: "))
        push(val)
    elif ch == 2:
        pop()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Selesai")
        break
    else:
        print("Salah pilih")