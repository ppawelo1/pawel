#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

def trojkat(a, b, c):
    """
    Funkcjabada możliwości zbudowania trójkąta z trzech podanych boków
    Funkcja zwraca True jeżeli sie da, False w przeciwnym wypadku
    """
    pass
    if a + b > c and b + c > a and a + c > b:
        return True
        
    return False
    
    #if a + b > c:
        #print ("True")
    #if a + b == a:
    #    print("False")
    #if a + b < b:
     #   print("False")
        
    return 

def main(args):
    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
   #a = 3
   #b = 4
   #c = 5
    #f trojkat(a, b, c):
    #   print("Da się")
    #else
    #   print("Ni hu hu")
    
    
    # = int(input('Podaj 1. bok: '))
    #rint(a)
   #b = int(input('Podaj 2. bok: '))
   #print(b)
   #c = int(input('Podaj 3. bok: '))
   #print(c)
   #print(trojkat(a, b, c))
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
