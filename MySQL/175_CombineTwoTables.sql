-- 175. Combine Two Tables
SELECT
    Person.FirstName,
    Person.LastName,
    Address.City,
    Address.State
FROM
    Person
    LEFT JOIN Address ON Person.PersonId = Address.PersonId;

-- 2nd solution
SELECT
    FirstName,
    LastName,
    City,
    State -- Select required columns from both tables
FROM
    Person -- Using NATURAL JOIN to automatically match common columns
    NATURAL LEFT JOIN Address;
