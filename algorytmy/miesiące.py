#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  miesiace.py
#  

def main(args):
	
	nazwa = ['','styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','paździenik','listopad','grudzień']
	
	a = 3
	
	while a > 0:
		a = a - 1
		miesiac = int(input("Podaj numer miesiąca: "))
		if miesiac > 12 or miesiac < 1:
			print("Błędne dane! ")
		else:
			print (nazwa[miesiac])
	return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))