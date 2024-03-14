-- list records of table second_table
-- only rows with valid name value
-- display score and name
-- in decending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
