-- Lists num of records having same score in our second_table.
-- Records ordered by desc count.
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
