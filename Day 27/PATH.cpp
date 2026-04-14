#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    
    // Count available pieces (lowercase letters)
    map<char, int> pieces;
    int bought = 0;
    
    for (int i = 0; i < (int)s.size(); i++) {
        if (isupper(s[i])) {
            // It's a puzzle - need a matching piece (lowercase version)
            char need = tolower(s[i]);
            if (pieces[need] > 0) {
                pieces[need]--;
            } else {
                bought++;
            }
        } else {
            // It's a piece - add to collection
            pieces[s[i]]++;
        }
    }
    
    cout << bought << endl;
    return 0;
}
