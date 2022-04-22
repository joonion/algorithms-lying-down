#include <iostream>
using namespace std;

void swap(int &x, int &y) {
    cout << "swap with a temporary variable:" << endl;
    int t = x;
    x = y;
    y = t;
}

int main() {
    int x = 10, y = 20;
    cout << "x = " << x << ", y = " << y << endl;
    swap(x, y);
    cout << "x = " << x << ", y = " << y << endl;
}