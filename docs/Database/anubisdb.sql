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
	abstract VARCHAR(500) NOT NULL,
	author VARCHAR(13) NOT NULL,
	category INTEGER NOT NULL,
	subcategory INTEGER NOT NULL,
	isExposed BOOLEAN NOT NULL,
	isPresented BOOLEAN NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL,

	FOREIGN KEY(author) REFERENCES authors(cpf),
	FOREIGN KEY(category) REFERENCES categories(code),
	FOREIGN KEY(subcategory) REFERENCES subcategories(code)

);


CREATE TABLE categories(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL

);


INSERT INTO categories(name, createdAt, modifiedAt) VALUES ("Teleeducação", "2019-03-03", "2019-03-03");
INSERT INTO categories(name, createdAt, modifiedAt) VALUES ("Teleassistência", "2019-03-03", "2019-03-03");
INSERT INTO categories(name, createdAt, modifiedAt) VALUES ("Tecnologias da Informação e Comunicação", "2019-03-03", "2019-03-03");

CREATE TABLE subcategories(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	category INTEGER NOT NULL,
	createdAt DATE NOT NULL,
	modifiedAt DATE NOT NULL,

	FOREIGN KEY(category) REFERENCES categories(code)
);

INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("TICs na Promoção e Prevenção à Saúde", 3, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("TICs na Educação Médica e das Profissões da Saúde", 3, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("TICs na Vigilância em Saúde", 3, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("Tecnologias disruptivas em Saúde", 3, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("Teleassistência / Telecuidado", 2, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("Telemedicina e Telessaúde aplicadas à Gestão na Saúde", 2, "2019-03-03", "2019-03-03");
INSERT INTO subcategories(name, category, createdAt, modifiedAt) VALUES ("Legislação e Normas em Telemedicina, Telessaúde e Saúde Digital", 1, "2019-03-03", "2019-03-03");
