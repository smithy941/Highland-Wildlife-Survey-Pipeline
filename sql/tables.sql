-- This script is written for MariaDB/MySQL
-- The InnoDB engine is used as it supports foreign keys

-- volunters
CREATE TABLE volunteers (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
) ENGINE=InnoDB;

-- survey sites
CREATE TABLE survey_sites (
    site_id INT AUTO_INCREMENT PRIMARY KEY,
    site_name VARCHAR(100),
    location VARCHAR(100)
) ENGINE=InnoDB;

-- species
CREATE TABLE species (
    species_id INT AUTO_INCREMENT PRIMARY KEY,
    species_name VARCHAR(100),
    conservation_status VARCHAR(100)
) ENGINE=InnoDB;

-- survey sessions
CREATE TABLE survey_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    volunteer_id INT,
    site_id INT,
    survey_date DATE,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id),
    FOREIGN KEY (site_id) REFERENCES survey_sites(site_id)
) ENGINE=InnoDB;

-- sightings
CREATE TABLE sightings (
    sighting_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT,
    species_id INT,
    count INT,
    FOREIGN KEY (session_id) REFERENCES survey_sessions(session_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id)
) ENGINE=InnoDB;

-- alerts
CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    species_id INT,
    alert_date DATE,
    FOREIGN KEY (species_id) REFERENCES species(species_id)
) ENGINE=InnoDB;