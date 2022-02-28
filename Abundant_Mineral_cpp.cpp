#include <iostream>
#include <map>
#include <string>
#include <iterator>

using namespace std;

int main() {
    
    map<char, int> m;
    int n;
    map<char, int>::iterator it;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            it = m.find(s[i]);
            if (it != m.end()) {
                it->second++;
            }
            else {
                m.insert(pair<char, int>(s[i], 1));
            }
        }
    }
    
    int high = 0;
    char c;
    
    for (it = m.begin(); it != m.end(); it++) {
        if (it->second > high) {
            high = it->second;
            c = it->first;
        }
    }
    
    cout << c;
    
    return 0;
}
