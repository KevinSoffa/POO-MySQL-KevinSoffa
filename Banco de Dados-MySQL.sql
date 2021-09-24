CREATE SCHEMA IF NOT EXISTS `projetoaeronave`;
USE `projetoaeronave`;

CREATE TABLE IF NOT exists `admin`(
	idAdm INT(11) NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    status int(11) NOT NULL,
    primary key(`idAdm`)
);

CREATE TABLE IF NOT exists `aeronaves`(
	idAeronave int(11) NOT NULL auto_increment,
    modelo VARCHAR(100) NOT NULL,
    ano int(4) NOT NULL,
    cor VARCHAR(30),
    tipo int(2),
    primary key(`idAeronave`)
);


INSERT INTO admin (nome,email,senha, status) VALUE ('kevin', 'kevin@gmail.com', 'and', 1);

SELECT * FROM admin;