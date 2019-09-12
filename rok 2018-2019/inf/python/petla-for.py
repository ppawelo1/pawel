#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
 

def main(args):
    
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    while a >= b:
        b = int(input("Błedny zakres"))
    
    if a >= b:
        print("Błędny zakres")
        #exit(0)
    
    for liczba in range(a, b):
        if liczba % 2 == 0:
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
