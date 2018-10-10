DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS oceny;
DROP TABLE IF EXISTS dane;

CREATE TABLE uczniowie(
	id INTEGER  PRIMARY KEY NOT NULL,
  numer ucznia TEXT(16),
  nazwisko TEXT(20),
	imie TEXT(16),
	imie2 TEXT(16)
);

CREATE TABLE dane(
  id INTEGER  PRIMARY KEY NOT NULL,
  numer ucznia TEXT(16),
  dzien INTEGER(2),
  miesiac INTEGER(1),
  rok INTEGER(2),
  miejsce_urodzenia TEXT,
  wojewodztwo TEXT
  FOREIGN KEY (uczen_id) REFERENCES uczen(id),
 );

CREATE TABLE oceny (
  id INTEGER  PRIMARY KEY NOT NULL,
  Zach TEXT(20),
  Rel INTEGER(1) DEFAULT "",
  Ety INTEGER(1) DEFAULT "",
  Jpol INTEGER(1) DEFAULT "",
  Jang INTEGER(1) DEFAULT "",
  Jniem INTEGER(1) DEFAULT "",
  Mat INTEGER(1) DEFAULT "",
  Hist INTEGER(1) DEFAULT "",
  Geog INTEGER(1) DEFAULT "",
  Biol INTEGER(1) DEFAULT "",
  Fiz INTEGER(1) DEFAULT "",
  Che INTEGER(1) DEFAULT "",,
  Tech INTEGER(1) DEFAULT "",
  Info INTEGER(1) DEFAULT "",
  Plas INTEGER(1 ,DEFAULT "",
  PO INTEGER(1),DEFAULT "",
  WF INTEGER(1)DEFAULT "",
  FOREIGN KEY (uczen_id) REFERENCES uczen(id),
);

