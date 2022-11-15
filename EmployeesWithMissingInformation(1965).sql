-- mysql
SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Salaries as s
ON e.employee_id = s.employee_id
WHERE s.salary is NULL
UNION
SELECT s.employee_id
FROM Employees AS e
RIGHT JOIN Salaries as s
ON e.employee_id = s.employee_id
WHERE e.name is NULL
ORDER BY employee_id ASC;