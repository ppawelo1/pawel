#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv
import os.path


def czy_jest(plik):
    """funkcja sprawdza istnienie pliku na dysku"""
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje".format(plik))
        return False
    return True


def dane_z_pliku(nazwa_pliku, separator=','):
    dane = []  # pusta lista na dane
    if not czy_jest(nazwa_pliku):
        return dane
    
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def kwerenda_1(cur):
    cur.execute("""
        SELECT * FROM magazyn
    """)

    """
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps) ORDER BY downloads DESC LIMIT 5;
    SELECT COUNT(name) FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT category, SUM(downloads) AS suma_pobran FROM fakeapps GROUP BY category ORDER BY suma_pobran DESC;


    """
    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:  # odczytywanie kolejnych rekordów
        print(tuple(row))  # drukowanie pól


def ile_kolumn(cur, tab):
    """ Funkcja sprawdza  i zwraca liczbe kolumn w podanej tabeli"""
    licznik = 0
    for kol in cur.execute("PRAGMA table_info('" + tab + "')" ):
        licznik += 1
    return licznik 

def main(args):
    #konfiguracja
    baza_nazwa = 'baza_prep'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    ####
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    # utworzenie tabeli w bazie
    if not czy_jest(baza_nazwa + '.sql'):
        return 0 
        
    with open(baza_nazwa + '.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych 
    for tab in tabele:
        ile = ile_kolumn(cur, tab)
        dane = dane_z_pliku(tab + roz, separator=',')
        ile_d = len(dane[0])
        
        if ile > ile_d: # trzeba dodać NONE
            dane2 = [] # tymczasowa liczba
            for r in dane:
                r.insert(0, None)
                dane2.append(r)
            dane = dane2
            
    ile = len(dane[0])
            
    cur.executemany('INSERT INTO ' + tab +
        ' VALUES(' + ','.join(['?'] * ile) + ')')

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
