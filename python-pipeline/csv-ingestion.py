import os
import csv

# csv files folder
incomingFolder = "data/incoming-csv"

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
                    print(row)

main()