import java.util.*;

class Node {
    int val;
    Node next;
    Node(int x) { val = x; next = null; }
}

public class Main {
    
    public static int minChanges(Node head, int n) {
        
        int[] original = new int[n];
        int[] sorted = new int[n];
        
        Node curr = head;
        
        // Step 1: copy values
        for (int i = 0; i < n; i++) {
            original[i] = curr.val;
            sorted[i] = curr.val;
            curr = curr.next;
        }
        
        // Step 2: sort
        Arrays.sort(sorted);
        
        // Step 3: count mismatches
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (original[i] != sorted[i]) {
                count++;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        Node head = null, tail = null;
        
        // Build linked list
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            Node newNode = new Node(x);
            
            if (head == null) {
                head = newNode;
                tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
        }
        
        System.out.println(minChanges(head, n));
        
        sc.close();
    }
}
