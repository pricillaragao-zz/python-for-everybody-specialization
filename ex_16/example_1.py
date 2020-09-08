# geoload.py
import sqlite3
from sqlite3.dbapi2 import Connection

api_key = False
if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

connection = sqlite3.connect("geodata.sqlite")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Locations (
    address TEXT,
    geodata TEXT)
    """
)

filehandle = open("where.data")
count = 0
print(filehandle)
for line in filehandle:
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more.")
        break

    address = line.strip()
    cursor.execute(
        "SELECT geodata FROM Locations WHERE address = ?",
        (memoryview(address.encode()),),
    )
    data = cursor.fetchone()[0]

    # connection.commit()
