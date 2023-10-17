-- Lists * records of second_table who's name column is not empty.
-- Order records in desc score order.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
