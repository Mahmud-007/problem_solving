#include<bits/stdc++.h>
using namespace std;

// you are given number of row and column 
// print a spiral matrix 
int ans[100][100];
void spiralMatrix(int row, int col){
    int left = 0, right = col-1, top = 0, bottom = row-1,dir = 1,c = 1;

    while(left<=right && top<=bottom){
        // left to right
        if (dir==1){
            for (int i=left;i<=right;i++){
                ans[top][i]=c++;
        }
        dir=2;
        top++;
    }
    // top to bottom
    else if(dir==2){
        for (int i=top;i<=bottom;i++){
            ans[i][right]=c++;
        }
        dir=3;
        right--;
    }
    // right to left
    else if(dir==3){
        for (int i=right;i>=left;i--){
            ans[bottom][i]=c++;
        }
        bottom--;
        dir=4;
    }
    else{
        for (int i=bottom;i>=top;i--){
            ans[i][left]=c++;
        }
        left++;
        dir=1;
    }
}
}
int main(){
    int n,m;
    cin>>n>>m;
    spiralMatrix(n,m);
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
    }
}