#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.stript() for x in rekord]  # usuwanie zbednych spacji
            dane.append(rekord)
    return dane


def main(args):
    con = sqlite3.connect('filmy.db')
    cur = con.cursor()  # utworzenie kursora

    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())

        filmy = dane_z_pliku('filmy.txt')
        filmy.pop(0)  # usunięcie pierwszego elementu listy
        cur.executemany('INSERT INTO filmy VALEUS(?, ?, ?, ?, ?)', filmy)

    con.commit()   # zatwierdzenie wszystkich operacji w bazie
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
