-- mysql
SELECT employee.name as Employee
FROM Employee employee
JOIN Employee manager 
ON employee.managerId = manager.id
AND employee.salary > manager.salary;