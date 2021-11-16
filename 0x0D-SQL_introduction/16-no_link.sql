-- lists all records of second_table in hbtn_0c_0
-- don't list rows without a name value
-- display score and name, in this order
-- records listed by descending order

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
