// QUEUE ARRAY BASED
// MENU

#include<stdio.h>
#include<conio.h> //kadang kadang bisa digunakan kadang2 gabisa dgunakan. kalo conio dipake, pake getch juga
#include<stdlib.h>
#define SIZE 10

void enQueue(int);
void deQueue();
void display(); // void untuk modul/prosedur

int queue[SIZE], front=-1, rear=-1;

int main()
{
    int value, choice;
    //clrscr();
    while(1){
        system("CLS");
        printf("\n\n*** MENU ***\n");
        printf("1. Enqueue\n2. Dequeue\n3. Tampilkan Data\n4. Selesai");
        printf("\npilih: ");
        scanf("%d", &choice);
        switch(choice){
            case 1: printf("ketik angka yang akan di enqueue: ");
                scanf("%d", &value);
                enQueue(value);
                break;
            case 2: deQueue();
                break;
            case 3: display();
                break;
            case 4: exit(0);
            default: printf("\nCoba lagi ya!!!");
        }
    }
}
void enQueue(int value){
    if (rear == SIZE-1)
        printf("\nAntrian sudah penuh, tidak bisa enqueue.");
    else {
        if (front == -1)
        front = 0;
        rear++;
        queue[rear] = value;
        printf("\nData berhasil ditambahkan.");
    }
    getch();
}
void deQueue(){
    if (front == rear)
        printf("\nAntrian kosong, tidak bisa di dequeue.");
    else {
        printf("\nData yang keluar: %d", queue[front]);
        front++;
        if (front == rear)
        front = rear = -1;
    }
    getch();
}
void display() {
    if (rear == -1)
        printf("\nAntrian kosong");
    else {
        int i;
        printf("\nData dalam antrian adalah: \n");
        for (i=front; i<=rear; i++)
        printf("%d\t", queue[i]);
    }
    getch();
}