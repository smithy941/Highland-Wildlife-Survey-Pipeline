import os
import csv
from datetime import datetime
import mysql.connector

# csv files folder
incomingFolder = "data/incoming-csv"

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="wildlife"
)

cursor = db.cursor()

errorLogFile = "data/error-logs/error-log.txt"

# check date is YYYY-MM-DD
def isValidDate(dateText):

    try:
        datetime.strptime(dateText, "%Y-%m-%d")
        return True

    except ValueError:
        return False

# check count is positive
def isValidCount(countText):

    try:
        count = int(countText)
        return count > 0

    except ValueError:
        return False

# check species exists in species table
def speciesExists(speciesName):

    speciesSql = "SELECT species_id FROM species WHERE species_name = %s"
    cursor.execute(speciesSql, (speciesName,))
    result = cursor.fetchone()

    if result is not None:
        return True
    else:
        return False

# check site exists in survey_sites table
def siteExists(siteName):

    siteSql = "SELECT site_id FROM survey_sites WHERE site_name = %s"
    cursor.execute(siteSql, (siteName,))
    result = cursor.fetchone()

    if result is not None:
        return True
    else:
        return False

# add rejected rows to error log
def logError(fileName, row, reason):

    # append adds to end. formatted string allows variables
    with open(errorLogFile, "a") as logFile:
        logFile.write(f"{fileName} | {reason} | {row}\n")

def main():

    # loop through files in folder
    for fileName in os.listdir(incomingFolder):

        # only process CSV files
        if fileName.endswith(".csv"):

            print("\nProcessing file:", fileName)

            # create file path
            filePath = incomingFolder + "/" + fileName

            # open file for reading
            with open(filePath, "r") as file:

                # read csv as dictionary
                reader = csv.DictReader(file)

                # expected headers
                requiredHeaders = [
                    "survey_date",
                    "volunteer_name",
                    "site_name",
                    "species_name",
                    "count"
                ]

                # check headers
                if reader.fieldnames != requiredHeaders:
                    print("Error, incorrect csv format in", fileName)
                    continue

                # loop through each row
                for row in reader:

                    if not isValidDate(row["survey_date"]):
                        logError(fileName, row, "Invalid date")
                        continue

                    if not isValidCount(row["count"]):
                        logError(fileName, row, "Invalid count")
                        continue

                    if not speciesExists(row["species_name"]):
                        logError(fileName, row, "Species not found")
                        continue

                    if not siteExists(row["site_name"]):
                        logError(fileName, row, "Site not found")
                        continue

                    # get ids needed for inserting into db
                    cursor.execute("SELECT volunteer_id FROM volunteers WHERE name = %s", (row["volunteer_name"],))
                    volunteerId = cursor.fetchone()[0] #[0] gets first value

                    cursor.execute("SELECT site_id FROM survey_sites WHERE site_name = %s", (row["site_name"],))
                    siteId = cursor.fetchone()[0]

                    cursor.execute("SELECT species_id FROM species WHERE species_name = %s", (row["species_name"],))
                    speciesId = cursor.fetchone()[0]

                    # insert survey session
                    cursor.execute(
                        "INSERT INTO survey_sessions (volunteer_id, site_id, survey_date) VALUES (%s, %s, %s)",
                        (volunteerId, siteId, row["survey_date"])
                    )
                    
                    sessionId = cursor.lastrowid

                    # insert sighting linked to sessionId
                    cursor.execute(
                        "INSERT INTO sightings (session_id, species_id, count) VALUES (%s, %s, %s)",
                        (sessionId, speciesId, int(row["count"]))
                    )

                    db.commit()

                    print("Inserted valid row:", row)

main()