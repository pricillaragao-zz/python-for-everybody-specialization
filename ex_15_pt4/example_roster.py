import sqlite3
import json
from pathlib import Path  # read documentation
from sqlite3 import Cursor

DB_NAME = "example_roster.sqlite"
Path(DB_NAME).touch()  # create the DB file
connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.executescript(
    """
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT);

    CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE);

    CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id));
"""
)


# filename = "roster_data_sample.json"
# with open("roster_data_sample.json") as filename:
#     str_data = open(filename).read()
#     print(str_data)

fname = input("Enter a file name: ")
if len(fname) > 1:
    fname = "roster_data_sample.json"

str_data = open(fname).read()
json_data = json.loads(str_data)
print(json_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    # print(name, title)

    cursor.execute("""INSERT OR IGNORE INTO User (name) VALUES ( ? )""", (name,))
    cursor.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = cursor.fetchone()[0]

    cursor.execute("""INSERT OR IGNORE INTO Course (title) VALUES ( ? )""", (title,))
    cursor.execute("SELECT id FROM Course WHERE title = ?", (title,))
    course_id = cursor.fetchone()[0]

    cursor.execute(
        """INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( ?, ? )""",
        (user_id, course_id),
    )

    connection.commit()
