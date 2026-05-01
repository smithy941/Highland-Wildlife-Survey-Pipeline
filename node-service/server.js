const express = require("express");
const mysql = require("mysql2");

// create server
const app = express();

const port = 3000;

// connect to database
const database = mysql.createConnection({
    host: "localhost",
    user: "student",
    password: "password123",
    database: "wildlife"
});


// route to get report e.g. http://localhost:3000/report/site/1
app.get("/report/site/:id", function (request, response)
{
    // get site id from url
    const siteId = request.params.id;

    // get site details
    const siteQuery = "SELECT * FROM survey_sites WHERE site_id = ?";

    database.query(siteQuery, [siteId], function (error, siteResult)
    { 

        // if database query fails send error message and stop
        if (error)
        {
            response.json({ message: "Error getting site" });
            return;
        }

        if (siteResult.length === 0)
        {
            response.json({ message: "Site not found" });
            return;
        }

        // get sightings for that site
        const sightingsQuery = `
            SELECT 
                survey_sessions.survey_date,
                volunteers.name,
                species.species_name,
                sightings.count
            FROM survey_sessions, volunteers, sightings, species
            WHERE survey_sessions.volunteer_id = volunteers.volunteer_id
            AND survey_sessions.session_id = sightings.session_id
            AND sightings.species_id = species.species_id
            AND survey_sessions.site_id = ?
        `;

        database.query(sightingsQuery, [siteId], function (error, sightingsResult)
        {
            if (error)
            {
                response.json({ message: "Error getting sightings" });
                return;
            }

            // build report object
            const report = {
                site: siteResult[0],
                total_sightings: sightingsResult.length,
                sightings: sightingsResult
            };

            // send back as json
            response.json(report);
        });
    });
});


// listen for requests on specified port
app.listen(port, function ()
{
    console.log("Server running on http://localhost:" + port);
});