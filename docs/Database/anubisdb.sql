CREATE DATABASE anubisdb;

USE anubisdb;

CREATE TABLE judges(
	cpf VARCHAR(13) NOT NULL PRIMARY KEY UNIQUE,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL

);

CREATE TABLE admins (
	cpf VARCHAR(13) NOT NULL PRIMARY KEY UNIQUE,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL

);

CREATE TABLE authors(
	cpf VARCHAR(13) NOT NULL PRIMARY KEY UNIQUE,
	name VARCHAR(255) NOT NULL,
	isStudent BOOLEAN NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL
);


CREATE TABLE papers (
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	author INTEGER NOT NULL,
	category INTEGER NOT NULL,
	subcategory INTEGER NOT NULL,
	isExposed BOOLEAN NOT NULL,
	isPresented BOOLEAN NOT NULL,
	judge INTEGER NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL,

	FOREIGN KEY(author) REFERENCES authors(cpf),
	FOREIGN KEY(category) REFERENCES categories(code),
	FOREIGN KEY(subcategory) REFERENCES subcategories(code),
	FOREIGN KEY(judge) REFERENCES judges(cpf)

);


CREATE TABLE categories(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL

);


INSERT INTO categories(name) VALUES ("Teleeducação");
INSERT INTO categories(name) VALUES ("Teleassistência");
INSERT INTO categories(name) VALUES ("Tecnologia da Informação e Comunicação");

CREATE TABLE subcategories(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	category INTEGER NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL

	FOREIGN KEY(author) REFERENCES authors(cpf)
);

INSERT INTO subcategories(name, category) VALUES ("TICs na Promoção e Prevenção à Saúde", 3);
INSERT INTO subcategories(name, category) VALUES ("TICs na Educação Médica e das Profissões da Saúde", 3);
INSERT INTO subcategories(name, category) VALUES ("TICs na Vigilância em Saúde", 3);
INSERT INTO subcategories(name, category) VALUES ("Tecnologias disruptivas em Saúde", 3);
INSERT INTO subcategories(name, category) VALUES ("Teleassistência / Telecuidado", 2);
INSERT INTO subcategories(name, category) VALUES ("Telemedicina e Telessaúde aplicadas à Gestão na Saúde", 2);
INSERT INTO subcategories(name, category) VALUES ("Legislação e Normas em Telemedicina, Telessaúde e Saúde Digital", 1);
