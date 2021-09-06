#include <iostream>

using namespace std;

int main(){
    
    int n;
    cin >> n;
    
    int sum1 = 0, sum2 = 0;
    
    int c = 0;
    
    while (n > 0){
        if (c % 2 == 0){
            sum1 += (n % 10);
        }
        else {
            sum2 += (n % 10);
        }
        n /= 10;
        c += 1;
    }
    
    cout << abs(sum2 - sum1);
    
    return 0;
}
