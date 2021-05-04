#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    
    int n, sum = 0, k = 0;
    cin >> n;
    
    int arr[n], fin[n];
    
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    sort(arr, arr + n);
    
    for (int i = 0; i < (n / 2); i++){
        sum += abs(arr[i] - arr[n - i - 1]);
        fin[k] = arr[i];
        k += 1;
        fin[k] = arr[n - i - 1];
        k += 1;
    }
    
    for (int i = 0; i < n; i++){
        if (i == (n - 1)){
            cout << fin[i] << endl;
        }
        else{
            cout << fin[i] << " ";
        }
    }
    
    cout << sum << endl;
    
    return 0;
}
