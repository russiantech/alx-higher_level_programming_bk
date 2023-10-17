-- Disp. 3 cities having highest avg temp. b/w July & August.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
