DROP TABLE IF EXISTS tbUCZNIOWIE;
DROP TABLE IF EXISTS tbKlasy;

CREATE TABLE tbUCZNIOWIE
{
	id INTEGER  PRIMARY KEY AUTOINTCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
  klasa TEXT,
  id_klasa INTEGER,
  egzHum NUMERIC NOT NULL DEFAULT 0,
  egzMat NUMERIC NOT NULL DEFAULT 0,
  egzJez NUMERIC NOT NULL DEFAULT 0,
  FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)
};

CREATE TABLE tbKlasy
{
	id INTEGER  PRIMARY KEY AUTOINTCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
};

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbKlasy VALUES (NULL, '2A', 2016, 2019);
INSERT INTO tbKlasy VALUES (NULL, '1C', 2017, 2020);
INSERT INTO tbUCZNIOWIE(id, imie, nazwisko, plec, id_klasa, egzHum, egzMat, egzJez)
VALUES (NULL, 'Adam', 'Słodowy', 0, 3, 70.5, 80, 90);
INSERT INTO tbUCZNIOWIE(id, imie, nazwisko, plec, id_klasa, egzHum, egzMat, egzJez)
VALUES (NULL, 'Pawel', 'Petelewicz', 0, 1, 87.7, 64, 99.9);

UPDATE tbUCZNIOWIE SET egzJez = 100 WHERE  id = 1;