#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  Program drukuje wypełniony prostokat o bokach podanych przez uzytkownika za pomoca podanego znaku.

def prostokat1(a, b, c):
    for i in range (a):
        for j in range (b):
            print(c, end='')
        print()
        
def prostokat2(a, b, c):
     for i in range (a):
        for j in range (b):
            if i 
            if j == 0 or b - 1:
                print(c, end='')
            else:
                print("", end='')
        print()
    
def main(args):
    a = int(input("Podaj 1 bok: "))
    b = int(input("Podaj 2 bok: "))
    c = input("Wypełnienie prostokata: ")
    
    print(prostokat1(a, b, c))
    
    return 0

if __name__ == '__main__':
    import sys 
    sys.exit(main(sys.argv))
