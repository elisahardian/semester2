// PROGRAM MENGGAMBARKAN SINGLE LINKED LIST. (C++)
// HEAD -> 42 -> 57 -> 23 -> 51 -> NULL

#include<iostream>
using namespace std;
//struktur node untuk menyimpan data dan pointer ke node berikutnya
struct Node{
    int data;
    Node* next;
};
//funngsi untuk menambahkan npde baru diakhiri Linked list
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

//fungsi untuk menampilkan seluruh node dalam linked list
void printList(Node* head){
    cout << "head -> ";
    Node* current = head;
    while (current != nullptr){
        cout << current -> data << " -> ";
        current = current -> next;
    }
    cout <<"NULL"<< endl;
}

int main(){
    Node* head = nullptr;
    //menambahkan node node kedalam linked list
    appendNode(&head, 42);
    appendNode(&head, 57);
    appendNode(&head, 23);
    appendNode(&head, 51);
    //menampilkan likend list
    printList(head);
    return 0;
}
