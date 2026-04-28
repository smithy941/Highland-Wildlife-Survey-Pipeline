-- These indexes improve query performance by finding rows faster instead of scanning the whole table.

-- This index improves queries that search by species_id
CREATE INDEX index_species
ON sightings(species_id);

-- This index improves queries that search by survey_date
CREATE INDEX index_date
ON survey_sessions(survey_date);

-- This shows how the database runs a query with species_id and confirms the index is being used
EXPLAIN
SELECT *
FROM sightings
WHERE species_id = 1;

-- This shows how the database runs a query with survey_date and confirms the index is being used
EXPLAIN
SELECT *
FROM survey_sessions
WHERE survey_date = '2026-01-01';