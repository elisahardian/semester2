//Contoh implementasi Stack C++ menggunakan Array (ada menu)

#include <iostream>
#include <iomanip>
#include <conio.h> //gapake ini juga bisa. kalo conio ini dihapus, yg getch() juga dihapus
using namespace std;
int stack[100], n=100, top=-1;

void push(int val) {
    if(top>= n-1)
    cout <<"Stack sudah penuh"<<endl;
    else {
        top++;
        stack[top]=val;
    }
}

void pop() {
    if(top<=-1)
    cout<<"Stack kosong"<<endl;
    else {
        cout<<"Elemen yang di pop = "<< stack[top] <<endl;
        top--;
    }
    getch(); //ini bisa dihapus
}

void display() {
    if(top>=0) {
        cout<<"Elemen stack adalah: ";
        for(int i=top; i>=0; i--)
        cout<<stack[i]<<" ";
        cout<<endl;
    } else
    cout<<"Stack kosong";
    getch(); //ini bisa dihapus
}

int main() {
    int ch, val;
    do {
        system("CLS");
        cout<<"1) Push ke Stack"<<endl;
        cout<<"2) Pop dari Stack"<<endl;
        cout<<"3) Tampilkan Stack"<<endl;
        cout<<"4) Selesai"<<endl;
        cout<<"Pilih: "<<endl;
        cin>>ch;
        switch(ch) {
            case 1: {
                cout<<"Ketik nilai yang akan di push:"<<endl;
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
    }while(ch!=4);
    return 0;
}