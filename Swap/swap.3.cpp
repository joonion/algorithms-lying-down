#include <iostream>
using namespace std;

void swap(int &x, int &y) {
    cout << "swap using xor operator:" << endl;
    x = y ^ y;
    y = x ^ y;
    x = x ^ y;
}

int main() {
    int x = 10, y = 20;
    cout << "x = " << x << ", y = " << y << endl;
    swap(x, y);
    cout << "x = " << x << ", y = " << y << endl;
}