#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
using namespace std;

int satisfiable(int n, int m, vector<vector<int>> F, vector<int>& S) {
    for (int v = 0; v < pow(2, n); v++) {
        // cout << "v = " << v << endl;
        for (int i = 0; i < m; i++) {
            int t = v;
            for (int j = 0; j < n; j++) {
                if (F[i][j] == 0)
                    t ^= (1 << (n - j - 1));
            }
            // cout << "\t" << bitset<3>(t) << endl;
            if (t == 0)
                return v;
        }
    }
    return -1;
}

int main() {
    int n, m; 
    cin >> n >> m;
    vector<vector<int>> F(m, vector<int>(n));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> F[i][j];
    vector<int> S;
    int result = satisfiable(n, m, F, S);
    if (result < 0)
        cout << "No" << endl;
    else
        cout << bitset<3>(result) << endl;
}