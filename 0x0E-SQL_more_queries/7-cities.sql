-- creates specifieed database
-- and table inside of database
-- fields: id (int) unique, not NULL and PK
-- state_id (int), not NULL and FK to reference id of states table
-- name (VARCHAR(256)) not NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states (id));
