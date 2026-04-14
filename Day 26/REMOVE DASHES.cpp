#include <iostream>
#include <string>
using namespace std;

void process_dashes(int n, string s) {
    string result = ""; // acts like a stack

    for (char ch : s) {
        if (ch == '_') {
            if (result.empty()) {
                cout << "-1";
                return;
            }
            result.pop_back(); // remove closest left letter
        } else {
            result.push_back(ch);
        }
    }

    if (result.empty()) {
        cout << "-1";
    } else {
        cout << result;
    }
}

int main() {
    int n;
    string s;

    cin >> n;
    cin >> s;

    process_dashes(n, s);

    return 0;
}
