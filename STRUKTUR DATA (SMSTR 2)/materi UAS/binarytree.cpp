#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    Node* root;

    void insertRecursively(Node*& node, int data) {
        if (!node) {
            node = new Node(data);
        } else if (data < node->data) {
            insertRecursively(node->left, data);
        } else if (data > node->data) {
            insertRecursively(node->right, data);
        }
        // Ignore duplicates (assuming no duplicates allowed)
    }

    void inorderTraversal(Node* node) {
        if (node) {
            inorderTraversal(node->left);
            cout << node->data << " ";
            inorderTraversal(node->right);
        }
    }

    void preorderTraversal(Node* node) {
        if (node) {
            cout << node->data << " ";
            preorderTraversal(node->left);
            preorderTraversal(node->right);
        }
    }

    void postorderTraversal(Node* node) {
        if (node) {
            postorderTraversal(node->left);
            postorderTraversal(node->right);
            cout << node->data << " ";
        }
    }

public:
    BinaryTree() : root(nullptr) {}

    void insert(int data) {
        insertRecursively(root, data);
    }

    void inorderTraversal() {
        cout << "Inorder Traversal: \n";
        inorderTraversal(root);
        cout << endl;
    }

    void preorderTraversal() {
        cout << "Preorder Traversal: \n";
        preorderTraversal(root);
        cout << endl;
    }

    void postorderTraversal() {
        cout << "Postorder Traversal: \n";
        postorderTraversal(root);
        cout << endl;
    }
};

int main() {
    BinaryTree tree;
    tree.insert(5);
    tree.insert(3);
    tree.insert(7);
    tree.insert(2);
    tree.insert(4);
    tree.insert(6);
    tree.insert(8);

    tree.inorderTraversal();
    tree.preorderTraversal();
    tree.postorderTraversal();

    return 0;
}