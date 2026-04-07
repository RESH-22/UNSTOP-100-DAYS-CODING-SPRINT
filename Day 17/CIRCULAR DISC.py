#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int minTimeToType(const std::string& word) {
    string s = word;
    
    // Step 1: Sort the string
    sort(s.begin(), s.end());
    
    int time = 0;
    char current = 'a'; // starting position
    
    for(char ch : s) {
        int diff = abs(ch - current);
        int move = min(diff, 26 - diff); // circular movement
        
        time += move;  // movement time
        time += 1;     // typing time
        
        current = ch;
    }
    
    return time;
}

int main() {
    string s;
    cin >> s;
    cout << minTimeToType(s);
    return 0;
}
