#include<bits/stdc++.h>
using namespace std;
int check[100];
int main()
{
    int n,e;
    cin>>n;
    vector<int>v;
    for (int i=0;i<n;i++){
        cin>>e;
        if (!check[e]){
            v.push_back(e);
            check[e]=1;
        }
    }
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
}