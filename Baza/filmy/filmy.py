#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def main(args):
    con = sqlite3.connect('filmy.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    filmy = dane_z_pliku('filmy.txt')
    filmy.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO filmy VALUES(?, ?, ?, ?, ?)', filmy)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
