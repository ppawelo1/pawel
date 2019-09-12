DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Subscribtion;
DROP TABLE IF EXISTS Orders;

CREATE TABLE Customers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	adres TEXT
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    subscribtion_id INTEGER,
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (subscribtion_id) REFERENCES Subscribtion(id)
);

CREATE TABLE Subscribtion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    price_per_month DECIMAL,
    subscription_length TEXT
);