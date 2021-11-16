-- creates a table called first_table in current database
-- description of table id INT, name VARCHAR(256)
-- if table exists, script should not fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
