#include <stdio.h>
#include <stdlib.h>

int main(){

    int n, d, re;

    scanf(" %d", &n);

    int arr[n];

    for (int i = 0; i < n; i++){
        scanf(" %d", &arr[i]);
    }

    scanf(" %d %d", &d, &re);

    int fi[n];

    for (int i = 0; i < n; i++){
        for (int j = i; j < n; j++){
            int x = arr[i] - arr[j];
            if ((arr[i] != arr[j]) && (abs(x) == d) && ((arr[i] ^ arr[j]) == re)){
                if (arr[i] < arr[j]){
                    printf("%d\t%d\n", arr[i], arr[j]);
                }
                else{
                    printf("%d\t%d\n", arr[j], arr[i]);
                }
            }
        }
    }

    return 0;
}
