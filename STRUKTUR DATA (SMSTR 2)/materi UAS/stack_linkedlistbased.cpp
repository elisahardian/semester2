//Contoh Implementasi Stack C++ menggunakan linked list (ada menu)
#include<iostream>
#include<stdlib.h>
using namespace std;
struct Node{
    int data;
    struct Node *next;
};
struct Node* top=NULL;

void push(int val){
    struct Node* newnode = (struct Node*) malloc(sizeof(struct Node));
    newnode -> data = val;
    newnode -> next = top;
    top = newnode;
}

void pop() {
    if(top==NULL)
    cout<<"struct kosong"<<endl;
    else {
        cout<<"Elemen yang di pop adalah: "<< top->data <<endl;
        top = top -> next;
    }
}

void display() {
    struct Node* ptr;
    if(top==NULL)
    cout<<"stack kosong";
    else {
        ptr = top;
        cout<<"Elemen Stack adalah: ";
        while (ptr != NULL){
            cout<< ptr -> data <<" ";
            ptr = ptr-> next;
        }
    } 
    cout<<endl;
}

int main() {
    int ch, val;
    cout<<"1) Push ke stack"<<endl;
    cout<<"2) Pop dari stack"<<endl;
    cout<<"3) Tampilkan stack"<<endl;
    cout<<"4) Selesai"<<endl;
    do {
        cout<<"Pilih: "<<endl;
        cin>>ch;
        switch(ch) {
            case 1: {
                cout<<"Ketik nilai yang akan di push: "<<endl;
                cin>>val;
                push(val);
                break;
            }
            case 2: {
                pop();
                break;
            }
            case 3: {
                display();
                break;
            }
            case 4: {
                cout<<"Selesai"<<endl;
                break;
            }
            default: {
                cout<<"Salah pilih"<<endl;
            }
        }
    } while (ch!=4);
    return 0;
}