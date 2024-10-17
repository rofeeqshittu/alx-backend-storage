-- Creates a table users following unique requirements.
CREATE TABLE IF NOT EXITS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
	);