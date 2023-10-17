-- Disp. max temp of each state, ordered by state names as `max_temp`.
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `state`;
