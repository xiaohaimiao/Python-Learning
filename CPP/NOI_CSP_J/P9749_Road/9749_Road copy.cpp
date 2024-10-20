#include <iostream>
#include <fstream>
using namespace std;
int main(){
    typedef long long ll;
    ifstream fin("road1.in");
    ofstream fout("road1.out");
    
    int n, d;
    fin >> n >> d;
    int v[n - 1];
    int a[n];
    for (int i = 0; i < n - 1; i++){
        fin >> v[i];
    }
    for (int i = 0; i < n; i++){
        fin >> a[i];
    }
    ll cost = 0;
    ll rest = 0;
    ll lowestCost = a[0];
    ll fuel = 0;
    ll shiJiZouDeLiang;
    for (int i = 0; i < n; i++){
        if (lowestCost <= a[0]){
            shiJiZouDeLiang = v[i] - rest;
        if (a[i] < lowestCost)
            lowestCost = a[i];
        if (shiJiZouDeLiang % d > 0)
        {
            fuel = shiJiZouDeLiang / d + 1;
            cost += fuel * lowestCost;
            rest = fuel * d - shiJiZouDeLiang;
        }
        else
        {
            fuel = shiJiZouDeLiang / d;
            cost += fuel * lowestCost;
            rest = 0;
        }
    }
    cout << cost << endl;
    fout << cost;
    cout.flush();
    fout.close();
    return 0;
}