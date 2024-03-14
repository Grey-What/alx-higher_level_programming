-- create a table id_not_null on server
-- with fields id (int) with default 1
-- and name (VARCHAR(256))
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
       );
