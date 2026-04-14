#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> find_anagram_indices(const string& s, const string& p) {
    vector<int> result;

    int n = s.size(), m = p.size();
    if (m > n) return result;

    vector<int> freqP(26, 0), window(26, 0);

    // Build frequency of pattern
    for (char c : p)
        freqP[c - 'a']++;

    // First window
    for (int i = 0; i < m; i++)
        window[s[i] - 'a']++;

    // Check first window
    if (window == freqP)
        result.push_back(0);

    // Slide the window
    for (int i = m; i < n; i++) {
        // Add new character
        window[s[i] - 'a']++;

        // Remove old character
        window[s[i - m] - 'a']--;

        if (window == freqP)
            result.push_back(i - m + 1);
    }

    return result;
}

int main() {
    string secret1, secret2;
    cin >> secret1 >> secret2;

    vector<int> res = find_anagram_indices(secret1, secret2);

    if (res.empty()) {
        cout << "Empty Array";
    } else {
        for (int i : res)
            cout << i << " ";
    }

    return 0;
}
