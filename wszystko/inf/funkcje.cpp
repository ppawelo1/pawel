/*
 * szblon.cpp
 */


#include <iostream>

using namespace std;

int dodaj(int a, int b)
{
   return a + b;
}
int odejmij(int a, int b)
{
   return a - b;
}
int pomnoz(int a, int b)
{
   return a * b;
}
int podziel(int a, int b)
{
   return a / b;
}

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
    
    cout << "Suma: " << dodaj(a, b) << endl;
    cout << "Róznica: " << odejmij(a, b) << endl;
    cout << "Iloczyn: " << pomnoz(a, b) << endl;
    cout << "Iloraz: " << podziel(a, b) << endl;
    
	return 0;
}

