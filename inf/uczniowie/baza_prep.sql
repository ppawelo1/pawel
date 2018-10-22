DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie(
	id INTEGER  PRIMARY KEY NOT NULL,
  imie TEXT,
  nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
  egz_hum INTEGER,
  egz_mat INTEGER,
  egz_jez INTEGER
   FOREIGN KEY (id_klasa) REFERENCES klasy(id),
);

CREATE TABLE klasy(
	id INTEGER  PRIMARY KEY AUTOINCREMENT,
  klasa TEXT,
  rok_naboru INTEGER,
  rok_matury INTEGER
);

CREATE TABLE przedmioty(
	id INTEGER  PRIMARY KEY AUTOINCREMENT,
  przedmiot TEXT,
  imie_naucz TEXT,
  nazwisko_naucz INTEGER,
  plec_naucz INTEGER
);

CREATE TABLE oceny(
	id INTEGER  PRIMARY KEY AUTOINCREMENT,
  datad date,
  id_uczen INTEGER,
  id_przedmiot INTEGER,
  ocena INTEGER
  FOREIGN KEY (id_uczen) REFERENCES oceny(id),
  FOREIGN KEY (id_przedmiot) REFERENCES oceny(id),
);


