#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py
#  
#  Copyright 2018  <>
#  

def liczby2():
    """
    Funkacja drukuje wszystkie liczby 2-cyfrowe, w których cyfry nie powtarzaja się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 11, 22, 33 itd.
    """
    ile = 0 #licznik
    for i in range (1,  10):
         for j in range (0,  10):
             if i != j:
                print("{}{} ".format(i, j), end='')
                ile = ile + 1
    return ile
    
    def liczby3():
    """
    Funkacja drukuje wszystkie liczby 3-cyfrowe, w których cyfry nie powtarzaja się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 111, 222, 333 itd.
    """
    ile = 0 #licznik
    for i in range (1,  10):
         for j in range (0,  10):
             if i != j:
                print("{}{} ".format(i, j), end='')
                ile = ile + 1
    return ile

def main(args):
    print("\n\nLiczb 2-cyfrowych:", liczby2())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
