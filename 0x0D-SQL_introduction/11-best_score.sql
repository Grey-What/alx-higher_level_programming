-- list records with score >= 10 in table second_table
-- display both the score and the name
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
