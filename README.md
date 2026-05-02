# Highland-Wildlife-Survey-Pipeline

## Requirements

Install the following before running:

Python 3  

sudo apt install python3
  

MariaDB / MySQL  

sudo apt install mariadb-server


MySQL Python Connector  

sudo apt install python3-mysql.connector

Node.js + npm  

sudo apt install nodejs npm

---

## CSV Ingestion

Reads CSV files, validates data, logs invalid rows and inserts valid data into the database.

### Run:

python3 python-pipeline/csv-ingestion.py


### Input:

data/incoming-csv/


### Output:

Inserts data into database  

Logs errors to:
data/error-logs/error-log.txt

---

## JSON Report (Node.js Service)

Creates a web service that returns sightings data as JSON.

### First-time setup (inside node-service folder):

cd node-service
npm init -y
npm install express mysql2

### Run the server:

node server.js

### Use:

Open in browser:

http://localhost:3000/report/site/1

Change last number to the site ID you wish to view

---

## XML Report Generation

Generates an XML report of endangered species alerts using an XSD schema.

### Run:

python3 python-pipeline/xml-alert-report.py

### Output:

data/reports/endangered-alert-report.xml

---

## XML Parsing

Reads partner survey data XML files and inserts it into the database.

### Run:

python3 python-pipeline/xml-import.py

### Input:

data/sample-xml/partner-survey.xml

### Output:
Inserts new survey session into database  
Inserts sightings into database  

---

## Notes

Database connection details are set in the scripts

Ensure the database and tables exist before running  

Stop the node server with ctrl + c
