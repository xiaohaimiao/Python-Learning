#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    typedef long long ll;

    ifstream fin("road2.in");   // input stream
    ofstream fout("road2.out"); // output stream

    // 初始化数据：来自于输入，或文件
    int n, d;
    fin >> n >> d;

    int v[n - 1];
    int a[n];
    for (int i = 0; i < n - 1; i++)
    {
        fin >> v[i];
    }
    for (int i = 0; i < n; i++)
    {
        fin >> a[i];
    }
    // 算法开始
    ll fuel = 0; // fuel：油
    ll rest = 0;
    ll shiJiZouDeLiang;
    ll lowestCost = a[0];
    ll cost = 0;
    for (int i = 0; i < n; i++)
    {
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
}
