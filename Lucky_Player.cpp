#include <cstring>
#include <iostream>

using namespace std;

int isEqual(int arr[], int n){
    for (int i = 0; i < n; i++){
        if (arr[i] != arr[0]){
            return 0;
        }
    }
    return 1;
}

int main(){
  
  /*Private Test Cases Failed*/
    
    int n, m;
    cin >> n >> m;
    
    char c[n][m];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> c[i][j];
        }
    }
    
    string x;
    cin >> x;
    
    int row[100], col[100], k = 0;
    
    for (int i = 0; i < x.length(); i++){
        for (int a = 0; a < n; a++){
            for (int b = 0; b < m; b++){
                if (x[i] == c[a][b]){
                    row[k] = a;
                    col[k] = b;
                    k += 1;
                }
            }
        }
    }
    
    char f[k]; 
    
    if (isEqual(row, k) == 1){
        for (int i = 0; i < m; i++){
            for (int j = 0; j < (m - i - 1); j++){
                if (c[row[0]][j] > c[row[0]][j + 1]){
                    swap(c[row[0]][j], c[row[0]][j + 1]);
                }
            }
        }
        
        for (int i = 0; i < m; i++){
            cout << c[row[0]][i];
        }
        cout << endl << "Lucky Player";
    }
    else if (isEqual(col, k) == 1){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < (n - i - 1); j++){
                if (c[j][col[0]] > c[j + 1][col[0]]){
                    swap(c[j][col[0]], c[j + 1][col[0]]);
                }
            }
        }
        
        for (int i = 0; i < n; i++){
            cout << c[i][col[0]];
        }
        cout << endl << "Lucky Player";
    }
    else{
        cout << "Unlucky Player";
    }

    
    return 0;
}
