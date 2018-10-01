DROP TABLE IF EXISTS miasta;
DROP TABLE IF EXISTS mieszkancy;
DROP TABLE IF EXISTS powierzchnia;

CREATE TABLE miasta (
	id INTEGER  PRIMARY KEY AUTOINCREMENT,
	city (30),
	province TEXT(35)
);

CREATE TABLE mieszkancy (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  people INTEGER,
  female INTEGER,
  age TEXT(20),
  data DATE
 );

CREATE TABLE powierzchnia (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  city_area DECIMAL,
  surface_green_area INTEGER,
  data DATE,
  FOREIGN KEY (miasta_id) REFERENCES mieszkancy(id),
);