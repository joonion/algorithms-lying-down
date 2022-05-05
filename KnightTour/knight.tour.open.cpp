#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, cnt;
vector<vector<int>> graph;
vector<int> mark;

void make_graph() {
    int imov[] = {-2, -1, 1, 2,  2,  1, -1, -2};
    int jmov[] = { 1,  2, 2, 1, -1, -2, -2, -1};
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            for (int k = 0; k < 8; k++) {
                int ni = i + imov[k];
                int nj = j + jmov[k];
                if (ni >= 0 && nj >= 0 && ni < n && nj < m)
                    graph[i*m + j].push_back(ni*m + nj);
            }
}

void tour(int kth, int v) {
    if (kth == n * m) {
        cnt++;
        // cout << "solution #" << cnt << ":" << endl;
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++)
        //         printf("%2d ", mark[i*m + j]);
        //     cout << endl;
        // }
    } else {
        for (int u: graph[v])
            if (mark[u] == 0) {
                mark[u] = kth + 1;
                tour(kth + 1, u);
                mark[u] = 0;
            }
    }
}

int main() {
    cin >> n >> m;
    graph.resize(n * m, vector<int>(0));
    make_graph();
    for (int v = 0; v < n * m; v++) {
        cout << v << ": ";
        for (int j = 0; j < graph[v].size(); j++)
            cout << graph[v][j] << " ";
        cout << endl;
    }

    int total = 0;
    for (int s = 0; s < n * m; s++) {
        mark.resize(n * m, 0);
        fill(mark.begin(), mark.end(), 0);
        mark[s] = 1; // mark starting vertex
        cnt = 0;
        tour(1, s);
        if (cnt > 0)
            cout << s << ": " << cnt << endl;
        total += cnt;
    }
    cout << "total = " << total << endl;
}