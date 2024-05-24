-- Link to the challenge
-- https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7199635229140004866-Mt0W/

-- I imported Excel BI's challenge data as a table named "Inventory" used in CTE3

WITH CTE1 AS (
	SELECT 1 AS MonthNumber
	UNION ALL
	SELECT MonthNumber + 1
	FROM CTE1
	WHERE MonthNumber < 12
),
CTE2 AS (
	SELECT	MonthNumber, 
		FORMAT(DATEFROMPARTS(2023, MonthNumber, 1), 'MMM') AS Month
	FROM CTE1
),
CTE3 AS (
	SELECT	a.Month,
		COALESCE(b.Incoming_Qty, 0) - COALESCE(b.Outgoing_Qty, 0) AS Result,
		a.MonthNumber
	FROM CTE2 a LEFT JOIN Inventory b
	ON a.Month = b.Month
)
SELECT	Month,
	SUM(Result) OVER (ORDER BY MonthNumber) AS Inventory
FROM CTE3
