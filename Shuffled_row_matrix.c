#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sortIt(int *arr, int n){
    for (int k = 0; k < n - 1; k++){
        for (int l = 0; l < (n - k - 1); l++){
            if (arr[l] > arr[l + 1]){
                int temp = arr[l];
                arr[l] = arr[l + 1];
                arr[l + 1] = temp;
            }
        }
    }
}

int main(){
    
    int m, n;
    scanf(" %d %d", &m, &n);
    
    int arr[m][n];
    
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            scanf(" %d", &arr[i][j]);
        }
    }
    
    int fir[n];
    int dec = 1;
    
    for (int a = 0; a < n; a++){
        fir[a] = arr[0][a];
    }
    
    sortIt(fir, n);
    
    for (int p = 1; p < m; p++){
        sortIt(arr[p], n);
        int z = !memcmp(fir, arr[p], sizeof(fir));
        if (!z){
            dec = 0;
            printf("Not Shuffled Row Matrix");
            break;
        }
    }
    
    if (dec == 1){
        printf("Shuffled Row Matrix");
    }
    
    return 0;
}