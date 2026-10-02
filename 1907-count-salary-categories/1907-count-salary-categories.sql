# Write your MySQL query statement below
SELECT
    category,
    COUNT(CASE 
        WHEN category = 'Low Salary' AND income < 20000 THEN 1
        WHEN category = 'Average Salary' AND income BETWEEN 20000 AND 50000 THEN 1
        WHEN category = 'High Salary' AND income > 50000 THEN 1
    END) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) AS categories
CROSS JOIN Accounts
GROUP BY category;