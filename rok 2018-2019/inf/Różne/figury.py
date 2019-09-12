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
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()
        
def choinka1(h, c):

    for i in range(h):
        for j in range(i + 1):
            print(c, end="")
        print()
        
def choinka2(h, c):

    for i in range(h):
        for j in range(h - i):
            print(c, end="")
        print()
        
def trojkat()
   
def main(args):
    #a = int(input("Podaj 1 bok: "))
    #b = int(input("Podaj 2 bok: "))
    #c = input("Wypełnienie prostokata: ")
    #h = int(input("Podaj wysokośc choinki: "))
    a, b, c = 10, 20, "$"
    print(prostokat1(a, b, c))
    print()
    print(prostokat2(a, b, c))
    print()
    h = 7
    choinka1(7, h)
    print()
    choinka2(7, h)
    print()
    
    #print(prostokat2(a, b, c))
    
    return 0

if __name__ == '__main__':
    import sys 
    sys.exit(main(sys.argv))
