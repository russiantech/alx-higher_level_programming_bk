-- create hbtn_0d_usa(DB) if it's not already there.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use created db
USE hbtn_0d_usa;
-- create table cities, probably for our clone project.
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
