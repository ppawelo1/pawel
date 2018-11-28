#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Petelewicz_przeszukiwanie.py
#  
#  Copyright 2018  <>
import random

def wypelnij(sztuk):
    for i in range(10):
        sztuk.append(random.randint(0, 50))
    print(sztuk)
    
def main(args):
    
    sztuk = []
    wypelnij(sztuk)
    i = int(input("Liczba: "))
    
    for j in range (len(sztuk)):
        if sztuka.cout(i) == 0 or i > 51:
            print("Element nieznaleziony")
            i += 1
            return
        else:
            print("Element znaleziony")
            return
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
