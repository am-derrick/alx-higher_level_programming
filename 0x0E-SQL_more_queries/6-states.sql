-- creates databse hbtn_0d_usa and table states
-- stats with id INT, unique, auto generated, can't be null and is a primary key
-- name VARCHAR(256) can;t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
