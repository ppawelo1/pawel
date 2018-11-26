#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py

import os
from peewee import *

baza_plik = 'test_orm.db'


baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egz_hum = DecimalField(default=0)
    egz_mat = DecimalField(default=0)
    egz_jez = DecimalField(default=0)
    
class Przedmioty(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()
    
class Oceny(BazaModel):
    data = dateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = IntegerField(default=0)
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Pzedmioty, Oceny])
    
    kl1 = Klasa(nazwa='2A', roknaboru=2012, rokmatury=2015)
    kl1.save()
    
    u1 = Uczen(imie='Jan', nazwisko='Kowalski', plec=False, klasa=kl1)
    u1.save()
    
    p1 = Przedmiot(przedmiot = 'matematyka', imie_naucz = 'Janusz', nazwisko_naucz ='Mroczkowski', plec_naucz=Flase)
    p1.save()
    
    o1 = Oceny(data='16.12.2018', uczen=i1, przedmiot=p1, ocena=6++
    o1.sve()
    baza.commit()
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
