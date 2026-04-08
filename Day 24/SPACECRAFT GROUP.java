import java.util.*;

public class Main {

    static class Pair {
        int pos;
        double time;

        Pair(int pos, double time) {
            this.pos = pos;
            this.time = time;
        }
    }

    public static int spaceshipFleets(int k, int[] pos, int[] speed) {

        int n = pos.length;
        Pair[] arr = new Pair[n];

        // Step 1: Compute time for each spaceship
        for (int i = 0; i < n; i++) {
            double time = (double)(k - pos[i]) / speed[i];
            arr[i] = new Pair(pos[i], time);
        }

        // Step 2: Sort by position descending
        Arrays.sort(arr, (a, b) -> b.pos - a.pos);

        int fleets = 0;
        double maxTime = 0;

        // Step 3: Traverse
        for (int i = 0; i < n; i++) {
            if (arr[i].time > maxTime) {
                fleets++;
                maxTime = arr[i].time;
            }
        }

        return fleets;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int[] pos = new int[n];
        int[] speed = new int[n];

        for (int i = 0; i < n; i++) {
            pos[i] = scanner.nextInt();
        }

        for (int i = 0; i < n; i++) {
            speed[i] = scanner.nextInt();
        }

        int result = spaceshipFleets(k, pos, speed);
        System.out.println(result);

        scanner.close();
    }
}
