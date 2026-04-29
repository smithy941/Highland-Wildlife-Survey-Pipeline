import os
import csv
from datetime import datetime
import mysql.connector

# csv files folder
incomingFolder = "data/incoming-csv"

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="wildlife"
)

cursor = db.cursor()

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

                # Expected headers
                requiredHeaders = [
                    "survey_date",
                    "volunteer_name",
                    "site_name",
                    "species_name",
                    "count"
                ]

                # Check headers
                if reader.fieldnames != requiredHeaders:
                    print("Error, incorrect csv format in", fileName)
                    continue

                # loop through each row
                for row in reader:

                    if not isValidDate(row["survey_date"]):
                        print("Invalid row, check date:", row)
                        continue

                    if not isValidCount(row["count"]):
                        print("Invalid row, check count:", row)
                        continue

                    if not speciesExists(row["species_name"]):
                        print("Invalid row, species not found:", row)
                        continue

                    if not siteExists(row["site_name"]):
                        print("Invalid row, site not found:", row)
                        continue

                    print("Valid row:", row)

main()