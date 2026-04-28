-- This stored procedure checks the population trend of a species between two dates
-- If the species is endangered and declining it automatically inserts a record into the alerts table

DELIMITER //

CREATE PROCEDURE check_species_trend(
    IN input_species_name VARCHAR(100),
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    DECLARE selected_species_id INT;
    DECLARE selected_status VARCHAR(50);
    DECLARE start_count INT DEFAULT 0; -- sets value at 0 so comparisons work
    DECLARE end_count INT DEFAULT 0;
    DECLARE trend_result VARCHAR(20);

    -- get species id and conservation status
    SELECT species_id, conservation_status
    INTO selected_species_id, selected_status
    FROM species
    WHERE species_name = input_species_name;

    -- count sightings on start date
    SELECT IFNULL(SUM(sightings.count), 0) -- If result is null replace with 0
    INTO start_count
    FROM sightings
    JOIN survey_sessions ON sightings.session_id = survey_sessions.session_id
    WHERE sightings.species_id = selected_species_id
    AND survey_sessions.survey_date = start_date;

    -- Count sightings on end date
    SELECT IFNULL(SUM(sightings.count), 0)
    INTO end_count
    FROM sightings
    JOIN survey_sessions ON sightings.session_id = survey_sessions.session_id
    WHERE sightings.species_id = selected_species_id
    AND survey_sessions.survey_date = end_date;

    -- determine trend
    IF end_count > start_count THEN
        SET trend_result = 'Increasing';
    ELSEIF end_count < start_count THEN
        SET trend_result = 'Decreasing';
    ELSEIF end_count = start_count THEN
        SET trend_result = 'Stable';
    END IF;

    -- if endangered and decreasing create alert for end date
    IF selected_status = 'Endangered' AND trend_result = 'Decreasing' THEN
        INSERT INTO alerts (species_id, alert_date)
        VALUES (selected_species_id, end_date);
    END IF;

    -- show result
    SELECT input_species_name AS species_name,
           start_count,
           end_count,
           trend_result;
END //

DELIMITER ;