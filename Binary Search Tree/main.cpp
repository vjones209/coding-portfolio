#include <iostream>
#include "bst.h"
#include "bst.cpp"

using namespace std;
using namespace BST;

int main() {
    BinarySearchTree bst;
    int input;

//User is asked for number in ascending order.
    cout << "Enter sorted integers (ascending order) to construct a binary search tree. Enter -1 to stop:\n";
    while (true) {
        cin >> input;
        if (input == -1)
            break;
        bst.insert(input);
    }

    cout << "\nHeight of the binary tree: " << bst.height() << endl;

    cout << "\nInorder traversal of the binary tree: ";
    bst.inorderTraversal();

    cout << "Preorder traversal of the binary tree: ";
    bst.preorderTraversal();

    cout << "Postorder traversal of the binary tree: ";
    bst.postorderTraversal();

    return 0;
}
