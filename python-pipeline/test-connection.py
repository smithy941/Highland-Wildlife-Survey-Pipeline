import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="student",
    password="password123",
    database="wildlife"
)

print("successful")