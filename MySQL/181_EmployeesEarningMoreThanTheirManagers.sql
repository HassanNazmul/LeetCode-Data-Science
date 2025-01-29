-- 181. Employees Earning More Than Their Managers

-- Solution 1: Using JOIN approach
SELECT employee.Name AS Employee
FROM Employee employee
INNER JOIN Employee manager ON employee.ManagerId = manager.Id
WHERE employee.Salary > manager.Salary;

-- Solution 2: Using subquery approach
SELECT e1.Name AS Employee
FROM Employee e1
WHERE e1.Salary > (
    SELECT e2.Salary 
    FROM Employee e2 
    WHERE e2.Id = e1.ManagerId
);


