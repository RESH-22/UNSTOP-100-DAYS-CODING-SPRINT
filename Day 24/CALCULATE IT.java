import java.util.*;

public class Main {

    public static int countExpressibleNumbers(int X, int Y) {
        Set<Integer> set = new HashSet<>();

        // Generate all 2^A * 3^B ≤ Y
        for (long p2 = 1; p2 <= Y; p2 *= 2) {
            for (long val = p2; val <= Y; val *= 3) {
                set.add((int) val);
            }
        }

        int count = 0;

        // Count numbers in range [X, Y]
        for (int num : set) {
            if (num >= X && num <= Y) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int X = scanner.nextInt();
        int Y = scanner.nextInt();

        int result = countExpressibleNumbers(X, Y);
        System.out.println(result);

        scanner.close();
    }
}
