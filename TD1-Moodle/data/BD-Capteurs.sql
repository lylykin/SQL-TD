
DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Capteur;

CREATE TABLE Capteur (
  numInventaire INT(10),
  refCapteur VARCHAR(50),
  typeCapteur VARCHAR(50),
  PRIMARY KEY (numInventaire)
);

CREATE TABLE Mesure (
  idMesure INT(10) PRIMARY KEY AUTO_INCREMENT,
  numInventaire INT(10),
  dateMesure DATETIME,
  valeur DECIMAL(6,2),
  FOREIGN KEY (numInventaire) REFERENCES Capteur(numInventaire)
);

INSERT INTO Capteur VALUES
(1,'TEMP:001','Température'),
(2,'HUM:Z32','Humidité'),
(3,'TEMP:007','Température'),
(4,'TEMP:865','Température'),
(5,'HUM:Z09','Humidité'),
(6,'TEMP:912','Température'),
(7,'TEMP:323','Température'),
(8,'HUM:Z51','Humidité'),
(9,'TEMP:347','Température'),
(10,'TEMP:725','Température'),
(11,'HUM:Z10','Humidité'),
(12,'TEMP:902','Température'),
(13,'HUM:ZH9','Humidité'),
(14,'TEMP:202','Température'),
(15,'CO2:ZXZ','CO2'),
(16,'CO2:ZYZ','CO2');

INSERT INTO Mesure (numInventaire,dateMesure,valeur) VALUES
(1,'2020-04-30 10:00:00',23.6),
(1,'2020-04-30 11:00:00',22.3),
(1,'2020-05-01 10:00:00',23.6),
(1,'2020-05-01 11:00:00',22.3),
(2,'2020-04-30 10:00:00',80.0),
(2,'2020-04-30 11:00:00',83.0),
(2,'2020-05-01 10:00:00',54.0),
(2,'2020-05-01 11:00:00',55.0);

