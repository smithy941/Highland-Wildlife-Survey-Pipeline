-- This script inserts sample data into the database
-- It contains over 50 records

-- volunteers
INSERT INTO volunteers (name, email) VALUES
('John Smith', 'john@gmail.com'),
('Jane Smith', 'jane@gmail.com'),
('David Smith', 'david@gmail.com'),
('Luke Smith', 'luke@gmail.com'),
('Katie Smith', 'katie@gmail.com');

-- survey sites
INSERT INTO survey_sites (site_name, location) VALUES
('Forest', 'Glencoe'),
('Valley', 'Portree'),
('Mountain', 'Fort William'),
('Loch', 'Inverness'),
('River', 'Skye');

-- species
INSERT INTO species (species_name, conservation_status) VALUES
('Red Squirrel', 'Endangered'),
('Beaver', 'Protected'),
('Osprey', 'Protected'),
('Golden Eagle', 'Endangered'),
('Fox', 'Common'),
('Deer', 'Common'),
('Otter', 'Protected'),
('Badger', 'Protected'),
('Pine Marten', 'Protected'),
('Wildcat', 'Endangered');

-- survey sessions
INSERT INTO survey_sessions (volunteer_id, site_id, survey_date) VALUES
(1, 1, '2026-01-01'),
(1, 1, '2026-01-02'),
(2, 2, '2026-01-03'),
(2, 2, '2026-01-04'),
(3, 3, '2026-01-05'),
(3, 3, '2026-01-06'),
(4, 4, '2026-01-07'),
(4, 4, '2026-01-08'),
(5, 5, '2026-01-09'),
(5, 5, '2026-01-10'),
(1, 2, '2026-01-11'),
(2, 3, '2026-01-12'),
(3, 4, '2026-01-13'),
(4, 5, '2026-01-14'),
(5, 1, '2026-01-15');

-- sightings 
INSERT INTO sightings (session_id, species_id, count) VALUES
(1,1,3),(1,2,2),(1,5,4),(1,7,2),
(2,1,2),(2,3,1),(2,6,5),(2,8,1),
(3,3,2),(3,4,1),(3,7,3),(3,9,2),
(4,2,3),(4,5,2),(4,8,4),(4,10,1),
(5,4,1),(5,6,3),(5,9,2),(5,6,2),
(6,3,2),(6,7,1),(6,10,1),(6,2,3),
(7,5,3),(7,8,2),(7,6,4),
(8,1,1),(8,9,2),(8,10,1),
(9,2,3),(9,6,5),(9,7,2),
(10,4,2),(10,5,3),(10,8,1),
(11,1,2),(11,3,1),(11,6,4),
(12,4,1),(12,7,2),(12,9,1),
(13,5,3),(13,8,2),(13,10,1),
(14,2,2),(14,6,3),(14,7,1),
(15,1,3),(15,4,2),(15,9,1);

-- alerts 
INSERT INTO alerts (species_id, alert_date) VALUES
(1, '2026-01-01'),
(1, '2026-01-02'),
(4, '2026-01-03'),
(10, '2026-01-04'),
(4, '2026-01-05'),
(10, '2026-01-06'),
(1, '2026-01-08'),
(10, '2026-01-08'),
(4, '2026-01-10'),
(1, '2026-01-11'),
(4, '2026-01-12'),
(10, '2026-01-13'),
(1, '2026-01-15'),
(4, '2026-01-15');