-- These SQL queries are used to analyse the data and demonstrate how the database can be used to extract insights.

-- all sightings
SELECT * FROM sightings;

-- species frequency
SELECT species_id, SUM(count) AS total_seen
FROM sightings
GROUP BY species_id;

-- species frequency by site 
SELECT survey_sessions.site_id, sightings.species_id, SUM(sightings.count) AS total_seen
FROM sightings
JOIN survey_sessions ON sightings.session_id = survey_sessions.session_id
GROUP BY survey_sessions.site_id, sightings.species_id;

-- volunteer activity rank
SELECT volunteer_id, COUNT(*) AS sessions_completed
FROM survey_sessions
GROUP BY volunteer_id
ORDER BY sessions_completed DESC;

-- sightings per session
SELECT session_id, SUM(count) AS total_animals
FROM sightings
GROUP BY session_id;

-- endangered species sightings
SELECT *
FROM sightings
WHERE species_id IN (1, 4, 10);

-- most active sites
SELECT site_id, COUNT(*) AS total_sessions
FROM survey_sessions
GROUP BY site_id
ORDER BY total_sessions DESC;

-- average sightings per session
SELECT AVG(count) AS avg_sightings
FROM sightings;

-- alert count per species
SELECT species_id, COUNT(*) AS alert_count
FROM alerts
GROUP BY species_id;

-- session on specific date 
SELECT *
FROM survey_sessions
WHERE survey_date = '2026-01-01';