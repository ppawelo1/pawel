#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#  

def nwd_klasyczny(a, b):
    while a != b:
        if a > b:
            a = a- b
        else:
            b = b - a
        #print(a)
    return a
    
        
def main(args):
    a = int(input("Podaj 1 liczbę: "))
    b = int(input("Podaj 2 liczbę: "))
    print("NWD1({}, {}) = {}".format(
                                    a, 
                                    b,
                                    nwd_klasyczny(a, b)
                                    ))
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
