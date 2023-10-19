-- select * cities records having `california` as state.
-- list * rows of column in our DB.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
