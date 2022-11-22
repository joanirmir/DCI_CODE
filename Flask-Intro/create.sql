
--Command to connect to the flask_intro database
\c flask_intro

-- Create a table called reminders

CREATE TABLE IF NOT EXISTS reminders (title VARCHAR(255), description Text);


-- To run this file
-- psql < create.sql - U postgres

-- Insert data

INSERT INTO reminders (title, description) VALUES('Mirjam is awesome', 'She is learning to code'),('Eat', 'Food is healthy'), ('Exercise', 'Get your heart moving');