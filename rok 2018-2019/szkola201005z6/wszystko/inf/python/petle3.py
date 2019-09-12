#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw3.py
#  Program wyświetla kwadraty kolejnych liczb naturalnych, począwszy od
#  zera a skończywszy na kwadracie liczby podanej przez użytkownika.


def main(args):
	liczba = int(input("Podaj liczbę: "))
	i = 0
	
	for i in range(liczba):
		i = i + 1
		print(i*i)
	return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))