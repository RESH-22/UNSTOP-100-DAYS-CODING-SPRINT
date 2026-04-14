#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Create node
TreeNode* createNode(int val) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

// Build tree from level order
TreeNode* buildTree(int arr[], int n) {
    if (n == 0 || arr[0] == -1) return NULL;

    TreeNode** nodes = (TreeNode**)malloc(n * sizeof(TreeNode*));

    for (int i = 0; i < n; i++) {
        if (arr[i] != -1)
            nodes[i] = createNode(arr[i]);
        else
            nodes[i] = NULL;
    }

    for (int i = 0; i < n; i++) {
        if (nodes[i] != NULL) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            if (left < n) nodes[i]->left = nodes[left];
            if (right < n) nodes[i]->right = nodes[right];
        }
    }

    TreeNode* root = nodes[0];
    free(nodes);
    return root;
}

// DFS
int dfs(TreeNode* root, int mask) {
    if (!root) return 0;

    // toggle bit
    mask ^= (1 << root->val);

    // leaf node
    if (!root->left && !root->right) {
        if ((mask & (mask - 1)) == 0)
            return 1;
        return 0;
    }

    return dfs(root->left, mask) + dfs(root->right, mask);
}

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    TreeNode* root = buildTree(arr, n);

    int result = dfs(root, 0);
    printf("%d\n", result);

    return 0;
}
