-- Link to the challenge
-- https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7194548579913371648-kqVz/

-- I imported Excel BI's challenge data as a table named "tblFruits"

WITH CTE1 AS
(
SELECT List1, COUNT(*) Count1
FROM tblFruits
GROUP BY List1
),
CTE2 AS
(
SELECT	List2, COUNT(*) Count2
FROM tblFruits
GROUP BY List2
)
SELECT	List1 Match, LEAST(Count1, Count2) Count 
FROM CTE1 INNER JOIN CTE2 
ON CTE1.List1 = CTE2.List2
