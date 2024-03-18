-- a script that lists all records of the table second_table.
-- Records greater than 10 are ordered in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score >= 10`
ORDER BY `score` DESC;
