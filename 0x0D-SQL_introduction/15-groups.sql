-- list number of records with the same score in the table second_table
-- result display score
-- and the number of records for each score with label number
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
