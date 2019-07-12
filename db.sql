CREATE USER 'manager'@'%' IDENTIFIED BY 'Manager#123';
CREATE DATABASE users;
GRANT ALL PRIVILEGES ON * . * TO 'manager'@'%';
FLUSH PRIVILEGES;
USE users;
CREATE TABLE users(
           name VARCHAR(100) NOT NULL,
           address VARCHAR(100) NOT NULL,
           phoneNo VARCHAR(15)
);
