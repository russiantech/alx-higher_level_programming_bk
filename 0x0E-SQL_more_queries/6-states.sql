-- create a DB, if it's not there already.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a db
USE hbtn_0d_usa;
-- creates states table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
