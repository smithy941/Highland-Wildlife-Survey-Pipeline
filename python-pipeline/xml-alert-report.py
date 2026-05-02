import mysql.connector
import xml.etree.ElementTree as ET


# report output files
xmlFile = "data/reports/endangered-alert-report.xml"
xsdFile = "data/reports/alert-report.xsd"


# connect to database
database = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="wildlife"
)

cursor = database.cursor(dictionary=True)


# get endangered species alert data
alertSql = """
SELECT
    alerts.alert_id,
    alerts.alert_date,
    species.species_name,
    species.conservation_status
FROM alerts, species
WHERE alerts.species_id = species.species_id
AND species.conservation_status = 'Endangered'
ORDER BY alerts.alert_date
"""

cursor.execute(alertSql)
alerts = cursor.fetchall()


# create root XML element (main tag)
root = ET.Element("endangered_species_alert_report")


# report title
title = ET.SubElement(root, "report_title")
title.text = "Endangered Species Alert Report"


# add alerts to XML
for alert in alerts:

    alertElement = ET.SubElement(root, "alert")

    alertId = ET.SubElement(alertElement, "alert_id")
    alertId.text = str(alert["alert_id"]) # str convert number to text

    alertDate = ET.SubElement(alertElement, "alert_date")
    alertDate.text = str(alert["alert_date"])

    species = ET.SubElement(alertElement, "species")

    speciesName = ET.SubElement(species, "species_name")
    speciesName.text = alert["species_name"]

    status = ET.SubElement(species, "conservation_status")
    status.text = alert["conservation_status"]

    trendData = ET.SubElement(alertElement, "trend_data")
    trendData.text = "Alert recorded for endangered species"

    recommendedAction = ET.SubElement(alertElement, "recommended_action")
    recommendedAction.text = "Review recent sightings and monitor this species closely"


# write xml file
tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write(xmlFile, encoding="utf-8", xml_declaration=True)

print("XML report created:", xmlFile)
print("Schema file used:", xsdFile)