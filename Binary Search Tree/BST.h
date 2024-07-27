#ifndef BST_H
#define BST_H

#include <iostream>
//Create header file for class definition implementation.
namespace BST {

    struct TreeNode {
        int data;
        TreeNode* left;
        TreeNode* right;

        TreeNode(int val);
    };

    class BinarySearchTree {
    private:
        TreeNode* root;

        // Private helper functions
        TreeNode* insertRecursive(TreeNode* root, int key);
        TreeNode* findRecursive(TreeNode* root, int key);
        void inorderTraversalRecursive(TreeNode* root);
        void preorderTraversalRecursive(TreeNode* root);
        void postorderTraversalRecursive(TreeNode* root);
        int heightRecursive(TreeNode* root);

    public:
        BinarySearchTree();
        void insert(int key);
        TreeNode* find(int key);
        void inorderTraversal();
        void preorderTraversal();
        void postorderTraversal();
        int height();
    };

} // namespace BST

#endif
