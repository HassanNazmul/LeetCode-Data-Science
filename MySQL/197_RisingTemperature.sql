-- 197. Rising Temperature

-- Solution 1: Using implicit join syntax
SELECT w1.id  -- Select the id of days with higher temperature
FROM Weather w1, Weather w2  -- Self join Weather table to compare consecutive days
WHERE w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)  -- Match current day with previous day (w2 is previous, w1 is current)
AND w1.temperature > w2.temperature;  -- Check if current day temp is higher than previous day


-- Solution 2: Using explicit JOIN syntax 
-- This solution achieves the same result but with clearer JOIN syntax
SELECT w1.id 
FROM Weather w1
JOIN Weather w2 
    ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)  -- Join condition matches current with previous day
WHERE w1.temperature > w2.temperature;  -- Filter for temperature increase

-- Note: DATE_ADD adds 1 day to w2.recordDate to match with w1.recordDate
-- w1 represents current day, w2 represents previous day