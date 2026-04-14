#include <stdio.h>
#include <stdlib.h>

int cmp_right(const void *a, const void *b) {
    return ((int*)a)[0] - ((int*)b)[0]; // ascending
}

int cmp_left(const void *a, const void *b) {
    return ((int*)b)[0] - ((int*)a)[0]; // descending
}

int user_logic(int n, int positions_cards[][2]) {
    int right[1000][2], left[1000][2];
    int r = 0, l = 0;

    // Separate positions
    for (int i = 0; i < n; i++) {
        if (positions_cards[i][0] > 0) {
            right[r][0] = positions_cards[i][0];
            right[r][1] = positions_cards[i][1];
            r++;
        } else {
            left[l][0] = positions_cards[i][0];
            left[l][1] = positions_cards[i][1];
            l++;
        }
    }

    // Sort
    qsort(right, r, sizeof(right[0]), cmp_right);
    qsort(left, l, sizeof(left[0]), cmp_left);

    int k = r < l ? r : l;
    int sum = 0;

    // Take alternating
    for (int i = 0; i < k; i++) {
        sum += right[i][1];
        sum += left[i][1];
    }

    // One extra
    if (r > l) {
        sum += right[k][1];
    } else if (l > r) {
        sum += left[k][1];
    }

    return sum;
}

int main() {
    int n;
    scanf("%d", &n);

    int positions_cards[1000][2];

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &positions_cards[i][0], &positions_cards[i][1]);
    }

    int result = user_logic(n, positions_cards);
    printf("%d\n", result);

    return 0;
}
