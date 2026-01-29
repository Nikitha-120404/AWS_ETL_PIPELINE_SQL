-- =========================================
-- AWS Glue SQL Transformation: Weather Data
-- =========================================

SELECT
    -- City name (explicitly cast to STRING for schema consistency)
    CAST(city AS STRING) AS city,

    -- Temperature value in Celsius
    CAST(temperature AS FLOAT) AS temperature,

    -- Humidity percentage
    CAST(humidity AS FLOAT) AS humidity,

    -- Categorize temperature into readable labels
    CASE
        WHEN temperature >= 35 THEN 'Hot'
        WHEN temperature >= 25 AND temperature < 35 THEN 'Warm'
        WHEN temperature >= 15 AND temperature < 25 THEN 'Cool'
        ELSE 'Cold'
    END AS temperature_category,

    -- Categorize humidity levels
    CASE
        WHEN humidity >= 70 THEN 'Humid'
        WHEN humidity >= 30 AND humidity < 70 THEN 'Normal'
        ELSE 'Dry'
    END AS humidity_category

-- Glue-provided source table / dynamic frame
FROM myDataSource

-- Filter out invalid or incomplete records
WHERE
    temperature IS NOT NULL
    AND humidity IS NOT NULL;
