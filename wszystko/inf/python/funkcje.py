#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szblon.py

# zasieg zmiennych;lokalny, globalny
def dodaj(a, b):
    return a + b
    
def odejmij(a, b):
    return a - b
    
def podziel(a, b):
    return a / b
   
def pomnoz(a, b):
    return a * b

def main(args):
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    
    print("Suma: ",  dodaj(a, b))
    print("Różnica: ", odejmij(a, b))
    print("Iloraz: ", podziel(a, b))
    print("Iloczyn: ", pomnoz(a, b))
    
    return 0
    
    # duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
