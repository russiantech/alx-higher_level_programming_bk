-- query/select from 2 tables where state-id matches with state-id in cities table.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
