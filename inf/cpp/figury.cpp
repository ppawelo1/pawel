/*
 * figury.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void prostokat(int a, int b, char znak) {
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= b; j++) {
            cout << setw(4) << i * j << " ";
            }
            cout << endl;
        }
}


int main(int argc, char **argv)
{
	int a, b; //deklaracja
    a = b = 0; //inicjacja
    //int a = 0; //definicja
    cout << "Podaj bok pierwszy: ";
    cin >> a;
    cout << "Podaj bok drugi: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat(a, b, znak);
	return 0;
}

