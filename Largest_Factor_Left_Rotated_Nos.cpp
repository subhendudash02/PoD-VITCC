#include <iostream>
#include <cmath>

using namespace std;

int left_rotate(int n){
    int k = n, rem = 0, c = 0;
    while (n > 0){
        rem = n % 10;
        c += 1;
        n /= 10;
    }
    return ((k - (pow(10, (c - 1)) * rem)) * 10) + rem;
}

int big_factor(int n){
    int big = 0;
    for (int i = 1; i < n; i++){
        if (n % i == 0 && i > big){
            big = i;
        }
    }
    return big;
}

int main(){
    int num;
    cin >> num;
    int arr1[4], arr2[4];
    
    int new_num = left_rotate(num);
    arr1[0] = num;
    arr1[1] = new_num;
    arr2[0] = big_factor(num);
    arr2[1] = big_factor(new_num);
    for (int i = 2; i < 4; i++){
        new_num = left_rotate(new_num);
        arr1[i] = new_num;
        arr2[i] = big_factor(new_num);
    }
    
    int high = 0, ind = 0;
    for (int i = 0; i < 4; i++){
        if (arr2[i] > high){
            high = arr2[i];
            ind = i;
        }
    }
    cout << arr2[ind] << "\n" <<arr1[ind];
    
    return 0;
}
