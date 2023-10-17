-- Lists * top records > 10 in `second_table` of hbtn_0c_0 DB of MySQL server.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
