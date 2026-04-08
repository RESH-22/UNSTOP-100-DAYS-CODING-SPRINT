import java.util.*;

public class Main {

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static void validateStackSequences(int[] pushed, int[] popped, boolean[] isValid, int[] primeCount) {

        Stack<Integer> stack = new Stack<>();
        int j = 0; // pointer for popped array

        // Simulate stack operations
        for (int x : pushed) {
            stack.push(x);

            // Keep popping while top matches popped[j]
            while (!stack.isEmpty() && j < popped.length && stack.peek() == popped[j]) {
                stack.pop();
                j++;
            }
        }

        // Check validity
        if (stack.isEmpty()) {
            isValid[0] = true;
            primeCount[0] = 0;
        } else {
            isValid[0] = false;

            int remaining = stack.size();
            int count = 0;

            // Count primes ≤ remaining
            for (int i = 2; i <= remaining; i++) {
                if (isPrime(i)) count++;
            }

            primeCount[0] = count;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] pushed = new int[n];
        int[] popped = new int[n];

        for (int i = 0; i < n; i++) {
            pushed[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            popped[i] = sc.nextInt();
        }

        boolean[] isValid = new boolean[1];
        int[] primeCount = new int[1];

        validateStackSequences(pushed, popped, isValid, primeCount);

        if (isValid[0]) {
            System.out.println("true");
        } else {
            System.out.println("false");
            System.out.println(primeCount[0]);
        }

        sc.close();
    }
}
