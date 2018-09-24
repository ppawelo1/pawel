DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS subscriptions;

CREATE TABLE customers (
	id INTEGER  PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	address TEXT
);

CREATE TABLE subscriptions (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  description TEXT,
  price_per_month DECIMAL,
  subscription_length TEXT
 );

CREATE TABLE orders (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  customers_id INTEGER,
  subscription_id INTEGER,
  purchase_data DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (subscriptions_id) REFERENCES subsctriptions(id)
);