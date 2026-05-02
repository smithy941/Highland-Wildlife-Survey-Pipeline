import xml.etree.ElementTree as ET
import mysql.connector


# XML file supplied by partner organisation
xmlFile = "data/sample-xml/partner-survey.xml"


# connect to database
database = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="wildlife"
)

cursor = database.cursor()


# read and parse XML file
tree = ET.parse(xmlFile)
root = tree.getroot()


# extract main survey details
surveyDate = root.find("survey_date").text
volunteerName = root.find("volunteer_name").text
siteName = root.find("site_name").text


# get volunteer id
cursor.execute("SELECT volunteer_id FROM volunteers WHERE name = %s", (volunteerName,))
volunteerId = cursor.fetchone()[0]


# get site id
cursor.execute("SELECT site_id FROM survey_sites WHERE site_name = %s", (siteName,))
siteId = cursor.fetchone()[0]


# insert survey session
cursor.execute(
    "INSERT INTO survey_sessions (volunteer_id, site_id, survey_date) VALUES (%s, %s, %s)",
    (volunteerId, siteId, surveyDate)
)

sessionId = cursor.lastrowid


# loop through each observation in XML
for observation in root.find("observations"):

    speciesName = observation.find("species_name").text
    count = observation.find("count").text

    # get species id
    cursor.execute("SELECT species_id FROM species WHERE species_name = %s", (speciesName,))
    speciesId = cursor.fetchone()[0]

    # insert sighting linked to survey session
    cursor.execute(
        "INSERT INTO sightings (session_id, species_id, count) VALUES (%s, %s, %s)",
        (sessionId, speciesId, int(count))
    )


database.commit()

print("Partner XML survey data imported successfully")