#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) : data(data), next(nullptr) {}
};

class Queue {
private:
    Node* front;
    Node* rear;

public:
    Queue() : front(nullptr), rear(nullptr) {}

    bool isEmpty() {
        return front == nullptr;
    }

    void enqueue(int data) {
        Node* new_node = new Node(data);
        if (isEmpty()) {
            front = new_node;
            rear = new_node;
        } else {
            rear->next = new_node;
            rear = new_node;
        }
    }

    int dequeue() {
        if (isEmpty()) {
            cout << "queue is empty" << endl;
            return -1; // or some error code
        } else {
            int dequeue_data = front->data;
            if (front == rear) {
                front = nullptr;
                rear = nullptr;
            } else {
                front = front->next;
            }
            return dequeue_data;
        }
    }

    int peek() {
        if (isEmpty()) {
            cout << "queue is empty" << endl;
            return -1; // or some error code
        } else {
            return front->data;
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "queue is empty" << endl;
        } else {
            Node* current = front;
            while (current != nullptr) {
                cout << current->data << " ";
                current = current->next;
            }
            cout << endl;
        }
    }
};

/*
int main() {
    Queue queue;
    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    queue.enqueue(40);
    cout << "queue setelah enqueue: " << endl;
    queue.display();
}
*/

int main(){
    Queue queue;
    while (true) {
        cout << "\nMenu:\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit" << endl;
        cout << "pilih (1/2/3/4/5): ";
        string choice;
        cin >> choice;

        if (choice == "1") {
            int data;
            cout << "data yang ingin dimasukkan ke antrian: ";
            cin >> data;
            queue.enqueue(data);
            cout << "data " << data << " telah dimasukkan kedalam antrian" << endl;
        } else if (choice == "2") {
            int removed_data = queue.dequeue();
            if (removed_data != -1) {
                cout << "data " << removed_data << " telah dihapus dari antrian" << endl;
            }
        } else if (choice == "3") {
            int front_data = queue.peek();
            if (front_data != -1) {
                cout << "elemen pertama dalam antrian: " << front_data << endl;
            }
        } else if (choice == "4") {
            cout << "isi dari antrian: " << endl;
            queue.display();
        } else if (choice == "5") {
            cout << "program berhenti" << endl;
            break;
        } else {
            cout << "pilihan tidak valid. coba lagi" << endl;
        }
    }

    return 0;
}