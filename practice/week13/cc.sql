CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  amount DECIMAL NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

