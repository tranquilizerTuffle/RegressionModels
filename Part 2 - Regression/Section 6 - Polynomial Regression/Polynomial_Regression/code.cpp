#include <stdio.h>
# include<bits/stdc++.h>

using namespace std;

int divide(int n,int d) {
    
    int t = 1;
    int q = 0;
 
    while (d <= n) {
        d <<= 1;
        t <<= 1;
    
    }

    while (t > 1) {
        d >>= 1;
        t >>= 1;
        if (n >= d) {
            n -= d;
            q += t;

        }
    }
    return q;
}


int multiply (int n, int m){
    int ans=0,ct=0;

    while (m){
        if(m%2==1){
            ans += (n << ct);
        }
        ct++;
        m=divide(m,2);
    }
    return ans;
}
  
void precisionCompute(int x, int y) 
{ 
    if (y == 0) { 
        cout << "Infinite" << endl; 
        return; 
    } 
    if (x == 0) { 
        cout << 0 << endl; 
        return; 
    } 
    
    if(x<0 && y<0){
        x=-x;
        y=-y;
    
    }
  
    if (((x > 0) && (y < 0)) || ((x < 0) && (y > 0))) { 
        cout << "-"; 
        x = x > 0 ? x : -x; 
        y = y > 0 ? y : -y; 
    } 
  
    int d = divide (x , y); 
  
    for (int i = 0; i <= 4; i++) { 
        cout << d; 
        x = x - multiply(y , d); 
        if (x == 0) 
            break; 
        x = multiply( x , 10); 
        d = divide (x , y); 
        if (i == 0) 
            cout << "."; 
    } 
} 
int main() 
{ 
    int x = 10, y = 21; 
    precisionCompute(x, y); 
    return 0; 
} 