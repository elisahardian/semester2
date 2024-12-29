//

#include <iostream>

using namespace std;

//Struktur node untuk menyimpan data dan pointer ke node berikutnya
struct Node{
    int data;
    Node* next;
};

//Fungsi untuk menambahkan node baru di akhir linked list
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

//Fungsi untuk menambahkan node baru setelah node tertentu
void insertAfter(Node* prevNode, int data){
    if (prevNode == nullptr){
        cout << "Node sebelumnya tidak ditemukan dalam linked list" << endl;
        return ;
    }

    Node* newNode = new Node;
    newNode -> data = data;
    newNode -> next = prevNode -> next;
    prevNode -> next = newNode;
}

//Fungsi untuk menyisipkan node baru sebelum node tertentu
void insertBefore(Node** head, Node* nextNode, int data){
    if (nextNode == nullptr){
        cout << "Node selanjutnya tidak ditemukan dalam linked list"<< endl;
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
    while (current -> next != nextNode){
        current = current -> next;
    }

    newNode -> next = current -> next;
    current -> next = newNode;
}

//Fungsi untuk menghapus node dengan nilai tertentu
void deleteNode(Node** head, int data){
    if (*head == nullptr){
        cout << "Linked list kosong"<< endl;
        return;
    }

    if((*head) -> data == data){
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

    cout <<"Node dengan nilai "<<data<<"tidak ditemukan dalam linked list"<< endl;
}

//Fungsi untuk menampilkan seluruh node dalam linked list
void printList(Node* head){
    cout <<"Head -> ";
    Node* current = head;
    while (current != nullptr){
        cout << current -> data << "-> ";
        current = current -> next;
    }
    cout <<"Null"<< endl;
}


int main(){
    Node* head = nullptr;

    //Menambahkan node node kedalam linked list
    appendNode(&head, 42);
    appendNode(&head, 57);
    appendNode(&head, 23);
    appendNode(&head, 51);

    cout<<"Linked list awal: "<< endl;
    printList(head);

    //Menambahkan node 10 setelah node 51
    Node* currentNode = head;
    while (currentNode -> data != 51){
        currentNode = currentNode -> next;
    }
    insertAfter(currentNode, 10);

    //Menyisipkan node 10 sebelum node 51
    currentNode = head;
    while (currentNode -> next -> data != 51){
        currentNode = currentNode -> next;
    }
    insertBefore(&head, currentNode -> next, 10);

    //menghapus node 23
    deleteNode(&head, 23);

    cout << "\nLinked list setelah modifikasi: "<< endl;
    printList(head);

    return 0;
}