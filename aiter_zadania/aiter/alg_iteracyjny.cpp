/*
 * alg_iteracyjny.cpp
 *
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    float iloczyn = 1;
    float a;
    cout << "Podaj liczbę całkowitą: ";
    cin >> n;
    for (int i=1; i <= n; i++) {
        cout << "Podaj liczbę: ";
        cin >> a;
        iloczyn *= a;
    }
    cout << iloczyn;
    return 0;
}
