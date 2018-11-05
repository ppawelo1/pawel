
DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS stanowisko;
DROP TABLE IF EXISTS placa;
DROP TABLE IF EXISTS kontakty;
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY NOT NULL,
    imie TEXT,
    nazwisko TEXT,
    kod_pocztowy TEXT,
    miasto_z varchar,
    ulica varchar,
    data_u varchar,
    miasto_u varchar

);

CREATE TABLE stanowisko (
     id_pracownika INTEGER(1),
     id_stanowisko INTEGER(1) PRIMARY KEY AUTOINCREMENT,
     stanowiska varchar,
    PRIMARY KEY (id_pracownika) REFERENCES pracownicy(id)
);

CREATE TABLE placa (
   id_p INTEGER,
   id_s INTEGER,
   placa INTEGER,
   data_z date
   PRIMARY KEY (id_p)  REFERENCES pracownicy(id)
   PRIMARY KEY (id_s)  REFERENCES stanowiska(id_stanowiska)
);

CREATE TABLE kontakty (
  id_pracownika INTEGER(1),
  typ_k boolean,
  kontakt varchar,
  uwagi varchar,
  PRIMARY KEY (id_pracownika) REFERENCES pracownicy(id)
);




