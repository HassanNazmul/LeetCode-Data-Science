-- 175. Combine Two Tables
-- First solution: Using explicit LEFT JOIN
SELECT
    Person.FirstName,    -- Select first name from Person table
    Person.LastName,     -- Select last name from Person table
    Address.City,        -- Select city from Address table
    Address.State        -- Select state from Address table
FROM
    Person              -- Start with Person table
    LEFT JOIN Address   -- Use LEFT JOIN to include all persons even without address
    ON Person.PersonId = Address.PersonId;  -- Join condition matching PersonId

-- Second solution: Using NATURAL JOIN
SELECT
    FirstName,          -- Select first name
    LastName,          -- Select last name
    City,              -- Select city
    State              -- Select state
FROM
    Person             -- Start with Person table
    NATURAL LEFT JOIN  -- Use NATURAL JOIN to automatically match common columns
    Address;           -- Address table to join with
