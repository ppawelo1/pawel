/*
 * szblon.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	float a, b;  // deklaracja zmiennej
    a = b = 0;  // inicjacja zmiennej
    
    cout << "Podaj 1. liczbę: ";
    cin >> a; 
    cout << a << endl; 
    
    cout << "Podaj 2. liczbę: ";
    cin >> b; 
    cout << b << endl;
    
    cout << "Suma: " << a + b << endl;
    cout << "Róznica: " << a - b << endl;
    cout << "Iloczyn: " << a * b << endl;
    cout << "Iloraz: " << a / b << endl;
    
	return 0;
}

