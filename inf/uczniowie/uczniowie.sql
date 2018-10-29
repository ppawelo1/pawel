
DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    plec BOOLEAN,
    id_klasa INTEGER NOT NULL,
    egz_hum NUMERIC NOT NULL DEFAULT 0,
    egz_mat NUMERIC NOT NULL DEFAULT 0,
    egz_jez NUMERIC NOT NULL DEFAULT 0,
    FOREIGN KEY (id_klasa) REFERENCES klasy (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);

DROP TABLE IF EXISTS klasy;
CREATE TABLE klasy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klasa TEXT(2),
    rok_naboru INTEGER,
    rok_matury INTEGER
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    przedmiot TEXT,
    imie_naucz TEXT,
    nazwisko_naucz TEXT,
    plec_naucz BOOLEAN
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datad DATE,
    id_uczen INTEGER NOT NULL,
    id_przedmiot INTEGER NOT NULL,
    ocena DECIMAL NOT NULL,
    FOREIGN KEY (id_uczen) REFERENCES uczniowie (id) ON DELETE NO ACTION ON UPDATE NO ACTION
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty (id) ON DELETE NO ACTION ON UPDATE NO ACTION
);




