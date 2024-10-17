#include<bits/stdc++.h>

using namespace std;

pair<int, int> GetEdge() {
    int a, b; 
    cin >> a >> b;
    return {a, b};
}

void SetAnswer(int s) {
    cout << s << endl;
    if (s == 0) {
        exit(0);
    }
}

int main(){
    int n;
    cin >> n;

    int distances[n][n];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if (i == j){
                distances[i][j] = 0;
            } else {
                distances[i][j] = INT_MAX;
            }
        }
    }


    while (true){
        auto [u, v] = GetEdge();
        u--; v--;

        if (distances[u][v] != INT_MAX && distances[u][v] % 2 == 0) {
            SetAnswer(0);
        }

        distances[u][v] = 1;
        distances[v][u] = 1;

        for (int i = 0; i < n; i++){
            if (distances[v][i] == INT_MAX || i == u) {
                continue;
            }
            for (int j = 0; j < n; j++){
                if (distances[u][j] == INT_MAX || j == v) {
                    continue;
                }
                distances[i][j] = distances[v][i] + distances[u][j] + 1;
                distances[j][i] = distances[i][j];
            }
        }
        SetAnswer(1);
    }
}