import java.util.*;

class Main {

    static class Point {
        int x, y, dist, index;

        Point(int x, int y, int index) {
            this.x = x;
            this.y = y;
            this.index = index;
            this.dist = x * x + y * y;
        }
    }

    public static void findKNearestPoints(List<int[]> points, int k, List<int[]> result) {

        List<Point> list = new ArrayList<>();

        // Store points with distance and index
        for (int i = 0; i < points.size(); i++) {
            int[] p = points.get(i);
            list.add(new Point(p[0], p[1], i));
        }

        // Sort by distance, then by index
        Collections.sort(list, (a, b) -> {
            if (a.dist != b.dist)
                return a.dist - b.dist;
            return a.index - b.index;
        });

        // Take first k points
        for (int i = 0; i < k; i++) {
            result.add(new int[]{list.get(i).x, list.get(i).y});
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        List<int[]> points = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            points.add(new int[]{x, y});
        }

        List<int[]> result = new ArrayList<>();
        findKNearestPoints(points, k, result);

        // Print result
        for (int[] p : result) {
            System.out.println(p[0] + " " + p[1]);
        }

        sc.close();
    }
}
