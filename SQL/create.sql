-- create a database called november

CREATE DATABASE november;

-- Linux: sudo -i -u postgres
-- Connect to a database

\c november

-- Create a Table calles users
-- name ()
-- location (string)
-- weight (floating number)

-- forgot!

-- UPDATE -> updating data of the table
-- Change the structure, we use ALTER

ALTER TABLE users ADD COLUMN id SERIAL PRIMARY KEY;

-- drop table (VERY RISKY!)
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    weight FLOAT
);
