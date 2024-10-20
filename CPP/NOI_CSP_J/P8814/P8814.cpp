#include <iostream>
#include <fstream>
using namespace std;
int main(){
    ifstream fin("decode2.in");
    ofstream fout("decode2.out");
    int k = 0;
    fin >> k;
    for (int i = 0; i < k; i++){
        int n, e, d;
        fin >> n >> e >> d;
        int q = 0, p = 0;
        int biaoJi = 0;
        for (int p = 1; p*p <= n; p++){
            if (n % p == 0){
                q = n / p;
                if ((p - 1) * (q - 1) + 1 == e * d){
                    cout << p << " " << q << endl;
                    fout << p << " " << q << endl;
                    biaoJi = 1;
                    break;
                }
            }
        }
        if (biaoJi != 1){
            cout << "NO" << endl;
            fout << "NO" << endl;
        }
    }
    return 0;
}