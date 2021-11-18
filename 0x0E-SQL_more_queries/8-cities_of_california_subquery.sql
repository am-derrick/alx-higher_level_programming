-- lists all cities of California that can be found in database hbtn_0d_usa
-- states table contains only one record where name = California, id can be different
-- sorted in ASC by cities.id


SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states where name = "California") ORDER BY id;
