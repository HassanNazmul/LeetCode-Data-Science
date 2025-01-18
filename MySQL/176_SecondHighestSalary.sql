-- 176. Second Highest Salary

-- Solution 1: Using subquery to find salary less than maximum
-- This approach finds the maximum salary that's less than the overall maximum
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < ( SELECT MAX(Salary) FROM Employee );

-- Solution 2: Using IFNULL with DISTINCT and ORDER BY
-- This approach:
-- 1. Gets distinct salaries
-- 2. Orders them in descending order
-- 3. Takes the second one (OFFSET 1)
-- 4. Returns NULL if no second highest salary exists
SELECT IFNULL(
    (SELECT DISTINCT Salary
     FROM Employee
     ORDER BY Salary DESC
     LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary;
