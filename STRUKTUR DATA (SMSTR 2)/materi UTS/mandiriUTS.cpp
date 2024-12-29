/*
// MEMBUAT. HEAD 42 57 23 51 NULL
#include <iostream>
using namespace std;
//struct node untuk menyimpab data dan pointe kenode berikutnya
struct Node{
    int data;
    Node* next;
};
//fungsi untuk menambahkan node baru diakhir linkedlist
void appendNode(Node** head, int data){
    Node* newNode = new Node;
    newNode -> data = data;
    newNode -> next = nullptr;
    if (*head == nullptr){
        *head = newNode;
        return;
    }
    Node* current = *head;
    while (current -> next != nullptr){
        current = current -> next;
    }
    current -> next = newNode;
}
//fungsi untuk menampilkan sebuah node dalam linkedlist
void printList(Node* head){
    cout <<"head-> ";
    Node* current = head;
    while (current != nullptr){
        cout << current -> data <<"->";
        current = current -> next;
    }
    cout <<"null"<<endl;
}
int main(){
    Node* head = nullptr;
    //menambahkan node kedalam linkedlist
    appendNode(&head, 42);
    appendNode(&head, 57);
    appendNode(&head, 23);
    appendNode(&head, 51);
    //menampilkan linkedlist
    printList(head);
    return 0;
}
*/

/*
//LIST = [42, 57, 23, 51] TUKAR POSISI LIST BERDASARKAN INPUTAN USER
#include<iostream>
#include<vector>
using namespace std;
int main(){
    //list awal
    vector <int> my_list = {42, 57, 23, 51};
    //menampilkan list saat ini
    cout<<"list saat ini: ";
    for (int x: my_list){
        cout <<x<< " ";
    }
    cout<<endl;
    //meminta input dari pengguna
    int pos1, pos2;
    cout <<"masukkan posisi elemen pertama yang ingin ditukar(0-based):";
    cin>>pos1;
    cout <<"masukkan posisi elemen kedua yang ingin ditukar(0-based):";
    cin>>pos2;
    //validasi input posisi
if (pos1 < 0 || pos1 >= my_list.size() || pos2<0 ||pos2 >= my_list.size()){
    cout <<"posisi yang dimasukkan tidak valid" <<endl;
    return 1;
}
    //menukar posisi element
    swap(my_list[pos1], my_list[pos2]);
    //menampilkan list setelah ditukar
    cout <<"list setelah ditular: ";
    for (int x:my_list){
        cout << x<<" ";
    }
    cout << endl;
    return 0;
}
*/



// MEMODIFIKASI SINGLE LL
#include<iostream>
using namespace std;
//structur node untuk menyimpan data dan pointer ke node berikutnya
struct Node{
    int data;
    Node* next;
};
// fungsi untuk menambahkan node baru diakhir ll
void appendNode(Node** head, int data){
    Node* newNode = new Node;
    newNode -> data = data;
    newNode -> next = nullptr;
    if (*head == nullptr){
        *head = newNode;
        return;
    }
    Node* current = *head;
    while (current -> next != nullptr){
        current = current -> next;
    }
    current -> next = newNode;

}
//fungsi untul menambahkan node baru setelah node tertentu
void insertAfter(Node* prevNode, int data){
    if (prevNode == nullptr){
        cout <<"node sebelumnta tidak ditemukan dalam ll "<<endl;
        return;
    }
    Node* newNode = new Node;
    newNode -> data = data;
    newNode -> next = prevNode -> next;
    prevNode -> next = newNode;
}
//fungsi untuk menyisipkan node baru sebelum node tertentu
void insertBefore(Node** head, Node* nextNode, int data){
    if (nextNode == nullptr){
        cout <<"node selanjutnya tidak ditemukan dalam linkedlist"<<endl;
        return;
    }
    Node* newNode = new Node;
    newNode -> data = data;
    if (*head == nextNode){
        newNode -> next = *head;
        *head = newNode;
        return;
    }
    Node* current = *head;
    while (current-> next != nextNode){
        current = current -> next;
    }
    newNode-> next = current -> next;
    current -> next = newNode;
}
//fungsi untuk menghapus node dengan nnilai tertentu
void deleteNode(Node** head, int data){
    if(*head == nullptr){
        cout <<"linkedlist kosong"<< endl;
        return;
    }
    if ((*head)-> data == data){
        Node* temp = *head;
        *head = (*head)-> next;
        delete temp;
        return;
    }
    Node* current = *head;
    while (current -> next != nullptr){
        if (current -> next -> data == data){
            Node* temp = current -> next;
            current -> next = current -> next -> next;
            delete temp;
            return;
        }
        current = current -> next;
    }
    cout <<"node dengan nilai "<<data<<"tidak ditemukan dalam ll"<<endl;
}
//fungsi untuk menampilkan seluruh node dalam mlinkedlist
void printList(Node* head){
    cout <<"head -> ";
    Node* current = head;
    while (current != nullptr){
        cout << current -> data <<"-> ";
        current=current-> next;
    }
    cout <<"null"<<endl;
}
int main(){
    Node* head = nullptr;
    //menambahkan node kedalam linked list
    appendNode(&head, 42);
    appendNode(&head, 57);
    appendNode(&head, 23);
    appendNode(&head, 51);
    cout<<"linkedlist awal: "<< endl;
    printList(head);
    //menambahkan node 10 setelah node 51
    Node* currentNode = head;
    while (currentNode -> data != 51){
        currentNode = currentNode -> next;
    }
    insertAfter(currentNode, 10);
    //menyisipkan node 10 sebelum node 51
    currentNode = head;
    while (currentNode -> next -> data != 51){
        currentNode = currentNode -> next;
    }
    insertBefore(&head, currentNode -> next, 10);
    //menghapus node 23
    deleteNode(&head, 23);
    cout <<"linkedlist setelah modifikasi: "<<endl;
    printList(head);
    return 0;
}





