/*
 * prostokat.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <cmath>

using namespace std;

int pole(int a, int b)
    {
        
    return a * b;
    }
    
int obwod(int a, int b)
    {
    return (2 * a) + (2 * b);
    }

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj długość boku a: ";
    cin >> a;
    cout << a;
      
    cout << endl << "Podaj długość boku b: ";
    cin >> b;
    cout << b;
    
    cout << endl << "Pole: " << pole(a, b) << endl;
    cout << endl << "Obwód: " << obwod(a, b) << endl;
    
    double liczba = 2;
    std::cout << sqrt(liczba);
return 0;
