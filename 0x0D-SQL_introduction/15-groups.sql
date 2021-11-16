-- lists number of records with same score in second_table in hbtn_0c_0
-- results should display the score, number of records with label number
-- sorted by number of records, descending

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
