DROP SCHEMA IF EXISTS test_db;
CREATE SCHEMA test_db;

DROP TABLE IF EXISTS items;
CREATE TABLE IF NOT EXISTS items(
  id              SERIAL PRIMARY KEY,
  name            VARCHAR(100) NOT NULL,
  count_freq      NUMERIC DEFAULT 0,
  description     VARCHAR(100) NULL
);

INSERT INTO items (name, description) VALUES ('apple', 'quantity: 4');
INSERT INTO items (name, description) VALUES ('milk', 'quantity: 4 pints');
INSERT INTO items (name, description) VALUES ('wine', 'reasonable, 1 bottle');
