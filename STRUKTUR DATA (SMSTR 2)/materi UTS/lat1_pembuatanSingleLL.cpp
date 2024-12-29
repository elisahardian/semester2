// PEMBUATAN SINGLE LINKED LIST. DENGAN HEAD - 42 - 57 - 23 - 51 - NULL

#include <iostream>
using namespace std;

//Struktur node untuk menyimpan data dan pointer ke node berikutnya
struct Node{
    int data;
    Node* next;
};

//Fungsi untuk menambahkan node baru diakhir linked list
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

//Fungsi untuk menampikan seluruh node dalam linked list
void printList(Node* head) {
    cout <<"Head -> ";
    Node* current = head;
    while (current != nullptr) {
        cout << current -> data << "-> ";
        current = current -> next;
    }
    cout <<"Null" << endl;
}

int main(){
    Node* head = nullptr;

    //Menambahkan node node kadalam linked list
    appendNode(&head, 42);
    appendNode(&head, 57);
    appendNode(&head, 23);
    appendNode(&head, 51);

    //Menampilkan linked list
    printList(head);
    return 0;
}