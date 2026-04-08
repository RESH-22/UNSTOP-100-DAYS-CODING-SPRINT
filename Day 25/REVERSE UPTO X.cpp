#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int data) {
        this->data = data;
        next = NULL;
    }
};

Node* reverseUptoX(Node* head, int x) {
    Node* curr = head;
    Node* prev = NULL;
    Node* next = NULL;

    Node* originalHead = head;
    bool found = false;

    while (curr != NULL) {
        next = curr->next;

        curr->next = prev;
        prev = curr;

        if (curr->data == x) {
            found = true;
            break;
        }

        curr = next;
    }

    if (found) {
        // Move curr one step forward properly
        Node* remaining = next;

        // connect tail of reversed part
        originalHead->next = remaining;

        return prev;
    }

    // If x not found → prev is new head (full reversed)
    return prev;
}

void printList(Node* head) {
    while (head != NULL) {
        cout << head->data << " ";
        head = head->next;
    }
}

int main() {
    int n;
    cin >> n;

    Node* head = NULL;
    Node* tail = NULL;

    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;

        Node* newNode = new Node(val);

        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    int x;
    cin >> x;

    head = reverseUptoX(head, x);

    printList(head);

    return 0;
}
