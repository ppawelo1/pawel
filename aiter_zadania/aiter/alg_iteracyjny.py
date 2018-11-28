#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    n = int(input("Podaj liczbę całkowitą: "))
    iloczyn = 1
    for i in range(1, n+1):
        a = float(input("Podaj liczbę: "))
        iloczyn *= a
    print(iloczyn)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
