-- 577. Employee Bonus

SELECT 
    Employee.name,    -- Select employee name from Employee table
    Bonus.bonus      -- Select bonus amount from Bonus table
FROM 
    Employee         -- Start with Employee table as base
LEFT JOIN 
    Bonus           -- Use LEFT JOIN to include all employees even if they have no bonus
    ON Employee.empId = Bonus.empId    -- Join condition matching employee IDs
WHERE 
    Bonus.bonus < 1000     -- Include employees with bonus less than 1000
    OR Bonus.bonus IS NULL -- Also include employees with no bonus (NULL)
ORDER BY 
    Employee.name;         -- Sort results alphabetically by employee name