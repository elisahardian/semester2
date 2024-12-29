//QUEUE LINKED LIST BASED
//MENU

#include<iostream>
#include<stdlib.h>
#include<conio.h> //kadang kadang bisa digunakan kadang2 gabisa dgunakan. kalo conio dipake, pake getch juga

using namespace std;
struct node {
    int data;
    struct node *next;
};
struct node* front = NULL;
struct node* rear = NULL;
struct node* temp;

void Insert() {
    int val;
    cout<<"Menambahkan data kedalam queue : "<<endl;
    cin>>val;
    if (rear == NULL) {
        rear = (struct node *)malloc(sizeof(struct node));
        rear -> next = NULL;
        rear -> data = val;
        front = rear;
    } else {
        temp = (struct node *)malloc(sizeof(struct node));
        rear -> next = temp;
        temp -> data = val;
        temp -> next = NULL;
        rear = temp;
    }
}
void Delete() {
    temp = front;
    if (front == NULL) {
        cout<<"Antrian kosong, tidak bisa dequeue"<<endl;
        getch();
        return;
    } else
    if (temp -> next != NULL) {
        temp = temp -> next;
        cout<<"Data yang keluar: "<<front -> data<<endl;
        free(front);
        front = temp;
    } else {
        cout<<"Data yang keluar adalah: "<<front -> data<<endl;
        free(front);
        front = NULL;
        rear = NULL;
    }
    getch();
}
void Display() {
    temp = front;
    if ((front == NULL) && (rear == NULL)) {
        cout<<"Antrian kosong."<<endl;
        getch();
        return;
    }
    cout<<"Data dalam antrian adalah: ";
    while (temp != NULL){
        cout<<temp -> data<<" ";
        temp = temp -> next;
    }
    cout<<endl;
    getch();
}

int main(){
    int ch;
    do {
        system("CLS");
        cout<<"1) Enqueue"<<endl;
        cout<<"2) Dequeue"<<endl;
        cout<<"3) Tampilkan data antrian"<<endl;
        cout<<"4) Selesai"<<endl;
        cout<<"pilih: "<<endl;
        cin>>ch;
        switch (ch) {
            case 1: Insert();
            break;
            case 2: Delete();
            break;
            case 3: Display();
            break;
            case 4: cout<<"Keluar"<<endl;
            break;
            default: cout<<"Coba lagi ya!!!"<<endl;
        }
    } while(ch != 4);
    return 0;
}