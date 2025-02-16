-- Step 1: Remove the 'refill liters' and 'refill gas' columns
ALTER TABLE measurements  
DROP COLUMN `refill liters`,  
DROP COLUMN `refill gas`;  

-- Step 2: Update 'specials' column: Replace empty values with 'no special'
UPDATE measurements  
SET specials = 'no special'  
WHERE specials = '' OR specials IS NULL;  

-- Step 3: Add the new 'snow' column (Boolean: 1 = snow, 0 = no snow)
ALTER TABLE measurements  
ADD COLUMN snow TINYINT(1) AFTER rain;  

-- Step 4: Fill 'snow' column based on 'specials' values
UPDATE measurements  
SET snow = IF(specials = 'snow', 1, 0);

-- Step 5: Replace commas with periods in the 'distance' and 'consume' columns
UPDATE measurements
SET distance = REPLACE(distance, ',', '.')
WHERE distance LIKE '%,%';

UPDATE measurements
SET consume = REPLACE(consume, ',', '.')
WHERE consume LIKE '%,%';

-- Step 6: Modify columns to FLOAT type
ALTER TABLE measurements  
MODIFY COLUMN distance FLOAT,  
MODIFY COLUMN consume FLOAT;

-- Step 7: Add the new column 'consume/100km' at the beginning
ALTER TABLE measurements  
ADD COLUMN `consume/100km` FLOAT FIRST;  

-- Step 8: Populate 'comsume/100km' using the formula (consume/distance) * 100
UPDATE measurements  
SET `consume/100km` = ROUND((consume / distance) * 100, 2);


-- Step 9: Calculate the Mean from temp_inside & Fill Missing values from temp_inside
SELECT ROUND(AVG(temp_inside)) AS mean_value
FROM measurements
WHERE temp_inside IS NOT NULL;

UPDATE measurements
SET temp_inside = 21
WHERE temp_inside IS NULL OR temp_inside = '';


-- Final check: Show the table content
SELECT * 
FROM technical_challenge_DA.measurements;

#--------------------------------------------------------------------------------------------------------------#

-- Q1: Which fuel type, in average, in the most consuming one? (Answer: SP98)

SELECT ROUND(AVG(`consume/100km`),2) AS avg_consume_per_100km, gas_type
FROM measurements
GROUP BY gas_type
ORDER BY avg_consume_per_100km;

-- Q2: How is the weather condition affecting the consumption of fuel? (Answer: Rain, snow, AC)

-- Presence Rain have a positive correlation with the vehicule consumption of fuel. AC is making the comsuption even higher. 
-- Despite a lack of data, snow seems also to a factor of high fuel comsuption

SELECT AC, rain, snow, sun, COUNT(`consume/100km`) AS trip_count, ROUND(AVG(`consume/100km`),2) AS avg_consume_per_100km
FROM measurements
WHERE AC=1 OR rain=1 OR snow=1 OR sun=1
GROUP BY AC, rain, snow, sun;

-- Q3: IS there a correlation with speed and fuel comsuption?
    
SELECT 
    CASE
        WHEN speed <= 25 THEN 'Slow:<=25km/h'
        WHEN speed BETWEEN 26 AND 35 THEN 'Rather Slow:26-35km/h'
        WHEN speed BETWEEN 36 AND 45 THEN 'Medium:36-45km/h'
        WHEN speed BETWEEN 46 AND 55 THEN 'Rather High:46-55km/h'
        WHEN speed >= 55 THEN 'High:>=55km/h'
    END AS speed_range,
    ROUND(AVG(`consume/100km`),2) AS avg_consume_per_100km, 
    COUNT(*) AS trip_count
FROM measurements
GROUP BY speed_range
ORDER BY avg_consume_per_100km DESC;


-- Q4: Is there a correlation with between outside temperature and fuel comsuption? 

SELECT
	CASE
		WHEN temp_outside <= 0 THEN 'freezing: 0 or below'
        WHEN temp_outside BETWEEN 1 AND 5 THEN 'cold: 1-5'
        WHEN temp_outside BETWEEN 6 AND 10 THEN 'rather cold: 6-10'
        WHEN temp_outside BETWEEN 11 AND 15 THEN 'cold mild: 11-15'
        WHEN temp_outside BETWEEN 16 AND 20 THEN 'mild: 16-20'
        WHEN temp_outside BETWEEN 21 AND 25 THEN 'rather warm: 21-25'
        WHEN temp_outside >= 26 THEN 'warm: 26 or more'
	END AS temp_outside_range,
    ROUND(AVG(`consume/100km`),2) AS avg_consume_per_100km, 
    COUNT(*) AS trip_count
    FROM measurements
GROUP BY temp_outside_range
ORDER BY avg_consume_per_100km DESC;
    

-- Q5: IS there a correlation with between temperature gap inside/outside and fuel comsuption? 

ALTER TABLE measurements  
ADD COLUMN `temperature_gap` FLOAT AFTER `temp_outside`;

UPDATE measurements  
SET `temperature_gap` = `temp_inside`-`temp_outside`;

SELECT 
	CASE
		WHEN temperature_gap <=-3 THEN 'negative difference'
        WHEN temperature_gap BETWEEN -2 AND 2 THEN 'no difference'
        WHEN temperature_gap  BETWEEN 3 AND 8 THEN 'minor positive difference'
        WHEN temperature_gap  BETWEEN 9 AND 14 THEN 'positive difference'
        WHEN temperature_gap  BETWEEN 15 AND 19 THEN 'rather significant positive difference'
        WHEN temperature_gap  >= 20 THEN 'significant positive difference'
	END AS temperature_gap_range,
ROUND(AVG(`consume/100km`),2) AS avg_consume_per_100km, COUNT(*) as trip_count
FROM measurements
GROUP BY temperature_gap_range
ORDER BY avg_consume_per_100km;
