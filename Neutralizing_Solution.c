#include <stdio.h>
#include <stdlib.h>

int main(){
    
    int n, *p;
    scanf(" %d", &n);
    
    p = (int *)malloc(n * sizeof(int));
    
    for (int i = 0; i < n; i++){
        scanf(" %d", p + i);
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < (n - i - 1); j++){
            if (*(p + j) > *(p + j + 1)){
                int temp = *(p + j);
                *(p + j) = *(p + j + 1);
                *(p + j + 1) = temp;
            }
        }
    }
    
    int b = 0;
    int k = 1;
    
    for (int i = *(p + 0); i <= *(p + n - 1); i++){
        b = 0;
        for (int j = 0; j < n; j++){
            int k = *(p + j);
            b += (k - i);
        }
        if (b == 0){
            printf("Yes\n");
            printf("%d\n", i);
            k = 0;
        }
    }
    
    if (k == 1){
        printf("No\n");
    }
    
    return 0;
}
