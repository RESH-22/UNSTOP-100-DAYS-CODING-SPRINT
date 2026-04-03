#include <iostream>
#include <string>

std::string follows_ab_pattern(const std::string& s) {
    bool seenB = false;

    for(char c : s) {
        if(c == 'b') {
            seenB = true;
        }
        else if(c == 'a' && seenB) {
            return "NO";
        }
    }

    return "YES";
}

int main() {
    std::string s;
    std::cin >> s;

    std::cout << follows_ab_pattern(s);

    return 0;
}
