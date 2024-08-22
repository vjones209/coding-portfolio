#include "bst.h"

using namespace BST;

//defining class definitions for binary search tree.
TreeNode::TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}

BinarySearchTree::BinarySearchTree() : root(nullptr) {}

void BinarySearchTree::insert(int key) {
    root = insertRecursive(root, key);
}

TreeNode* BinarySearchTree::insertRecursive(TreeNode* root, int key) {
    if (root == nullptr)
        return new TreeNode(key);
    if (key < root->data)
        root->left = insertRecursive(root->left, key);
    else if (key > root->data)
        root->right = insertRecursive(root->right, key);
    return root;
}

TreeNode* BinarySearchTree::find(int key) {
    return findRecursive(root, key);
}

TreeNode* BinarySearchTree::findRecursive(TreeNode* root, int key) {
    if (root == nullptr || root->data == key)
        return root;
    if (key < root->data)
        return findRecursive(root->left, key);
    return findRecursive(root->right, key);
}

void BinarySearchTree::inorderTraversal() {
    inorderTraversalRecursive(root);
    std::cout << std::endl;
}

void BinarySearchTree::inorderTraversalRecursive(TreeNode* root) {
    if (root) {
        inorderTraversalRecursive(root->left);
        std::cout << root->data << " ";
        inorderTraversalRecursive(root->right);
    }
}

void BinarySearchTree::preorderTraversal() {
    preorderTraversalRecursive(root);
    std::cout << std::endl;
}

void BinarySearchTree::preorderTraversalRecursive(TreeNode* root) {
    if (root) {
        std::cout << root->data << " ";
        preorderTraversalRecursive(root->left);
        preorderTraversalRecursive(root->right);
    }
}

void BinarySearchTree::postorderTraversal() {
    postorderTraversalRecursive(root);
    std::cout << std::endl;
}

void BinarySearchTree::postorderTraversalRecursive(TreeNode* root) {
    if (root) {
        postorderTraversalRecursive(root->left);
        postorderTraversalRecursive(root->right);
        std::cout << root->data << " ";
    }
}

int BinarySearchTree::height() {
    return heightRecursive(root);
}

int BinarySearchTree::heightRecursive(TreeNode* root) {
    if (root == nullptr)
        return 0;
    int leftHeight = heightRecursive(root->left);
    int rightHeight = heightRecursive(root->right);
    return std::max(leftHeight, rightHeight) + 1;
}
