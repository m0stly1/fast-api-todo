CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE todo (
    id int NOT NULL AUTO_INCREMENT,
    title varchar(255),
    status varchar(255),
    PRIMARY KEY (id)
);

INSERT INTO todo (title, status) VALUES ("watch The Matrix Resurrections", "todo");
INSERT INTO todo (title, status) VALUES ("watch The Book of Boba Fett", "doing");
INSERT INTO todo (title, status) VALUES ("watch The Mandalorian", "done");