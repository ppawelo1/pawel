#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#  
import sqlite3


def kwerenda(cur):
    cur.execute("""
      WITH srednie AS (
         SELECT nazwisko, imie, AVG(ocena) AS sred FROM uczniowie
         INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
         GROUP BY uczniowie.id
      ) SELECT COUNT(nazwisko)  FROM srednie
      WHERE sred > 3.5 OREDER BY sred DESC 
    """)
    
     #WITH srednie AS (
         #SELECT nazwisko, imie, AVG(ocena) AS sred FROM uczniowie
         #INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
         #GROUP BY uczniowie.id
      #) SELECT nazwisko, imie, sred FROM srednie
      #WHERE sred > 3.5 OREDER BY sred DESC
       
    # SELECT klasa, AVG(egz_mat) AS srm FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY srm DESC
    # SELECT klasa, AVG(egz_mat) FROM klasy INNER JOIN klasy ON klasy.id=uczniowie.id_klasa WHERE klasy.id=(SELECT klasy.id FROM klasy WHERE klasa='1A' AND rok_naboru=2012)
    # SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id WHERE klasa='1A' AND rok_naboru=2012
    # SELECT MAX(egz_mat), MINegz_mat) FROM uczniowie 
    # SELECT AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM uczniowie 
    # LIMIT 5
    # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 OREDER BY nazwisko ASC
    # SELECT COUNT(id) FROM uczniowie WHERE plec=1
    # SELECT COUNT(id) FROM uczniowie WHERE imie LIKE '%a'
    # SELECT id FROM uczniowie WHERE imie='Anna' AND nazwisko='Ignaczuk'
    # % to dowolny ciąg znaków, dowolnej długości
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
        

def main(args):
     # KONFIGURACJA #########
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
