
DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS stanowisko;
DROP TABLE IF EXISTS placa;
DROP TABLE IF EXISTS kontakty;
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY NOT NULL,
    imie TEXT,
    nazwisko TEXT,
    kod_pocztowy TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_u TEXT,
    miasto_u TEXT

);

CREATE TABLE stanowisko (
    id_stanowisko INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowiska TEXT

);

CREATE TABLE placa (
   id_p INTEGER NOT NULL,
   id_s INTEGER NOT NULL,
   placa INTEGER,
   data_z DATE,
   PRIMARY KEY (id_p)  REFERENCES pracownicy(id),
   PRIMARY KEY (id_s)  REFERENCES stanowiska(id_stanowiska)
);

CREATE TABLE kontakty (
  id_pracownika INTEGER NOT NULL,
  typ_k BOOLEAN,
  kontakt STRING,
  uwagi TEXT,
  PRIMARY KEY (id_pracownika) REFERENCES pracownicy(id_pracownika)
);




