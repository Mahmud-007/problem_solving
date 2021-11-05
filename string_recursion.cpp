#include<bits/stdc++.h>
using namespace std;
void f_callded(string s,int st,int e){
    if (st>e){
        return;
    }
    cout<<s[e]<<endl;
    f_callded(s,st,e-1);

}
int main(){
    string s;
    cin>>s;
    f_callded(s,0,s.length()-1);
}