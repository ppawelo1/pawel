DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS przedmiotu;
DROP TABLE IF EXISTS dane;

CREATE TABLE uczniowie(
	id_ucznia INTEGER  PRIMARY KEY,
  nazwisko TEXT,
	imie TEXT,
	ulica TEXT,
  dom TEXT,
  id_klasy TEXT
);

CREATE TABLE oceny(
  id_ucznia INTEGER,
  ocena TEXT(16),
  data DATE,
  id_przedmiotu INTEGER,
  FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
  FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia)
 );

CREATE TABLE przedmioty(
  id_przedmiotu PRIMARY KEY,
  Nazwa przedmiotu TEXT,
  Nazwisko_naucz TEXT,
  Imie_naucz TEXT
);
