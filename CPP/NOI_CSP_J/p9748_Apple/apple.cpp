#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int n, ans1 = 0, ans2 = 0;
    //cin >> n;
    n = 8;
    while (n > 0)
    {
        ans1 ++;
        if (ans2 == 0 && n % 3 == 1){
            ans2 = ans1;
        }
        n -= (n + 2) / 3;
    }

    cout << ans1 << " " << ans2 << endl;
    return 0;
}