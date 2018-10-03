#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby.py
#  
 
def main(args):

	suma = 0
	liczby = []
	a = int(input("podaj dowolną liczbę: "))
	
	liczby = list(map(int, str(a)))

	print (sum(liczby))
	return 0
	

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))