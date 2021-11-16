-- lists all records wit a score >= 10 in second_table in database hbtn_0c_0
-- displays score and name, in this order
-- scores are ordered, top first

SELECT score, name FROM second_table WHERE score >= 10, ORDER BY score DESC;
