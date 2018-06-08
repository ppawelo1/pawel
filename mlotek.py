#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    # print("Wylosowano:", liczba)  # pobieranie danych od uzytkownika
    for i in range(3):
        print("Próba", i + 1)
        odp = input("Podaj liczbe od 1 do 10; ")  # losowanie liczby
        print("Podałeś:", odp)

        if liczba == int(odp):  # pobieranie odp z wylosowana liczbą
            print("Zgadłeś!")
            break  # przerwanie działania pętli
        elif i == 2:
            print("wylosowano;" liczba)
        else:
            print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
