CREATE DATABASE real_estate_ml;

CREATE USER 'real_estate_ml_agent'@'%' identified by 'SuPeRsEcReTpWd';

GRANT ALL PRIVILEGES ON real_estate_ml.* TO 'real_estate_ml_agent'@'%';

USE real_estate_ml

CREATE TABLE property (
	id INT(10) UNSIGNED AUTO_INCREMENT,
	rooms INT(10) NOT NULL,
	distance FLOAT NOT NULL,
	post_code INT(10) NOT NULL,
	property_count INT(10) NOT NULL,
	price FLOAT NOT NULL,
	property_type CHAR(1),
	PRIMARY KEY (id)
) ENGINE=InnoDB;