import sqlite3
from pathlib import Path  # read documentation
from sqlite3 import Cursor


DB_NAME = "example.sqlite"
Path(DB_NAME).touch()  # create the DB file

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


# def create_table(cursor: Cursor):
cursor.executescript(
    """
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    email TEXT);
    
    CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT);
    
    CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id));
          
          
"""
)

cursor.executescript(
    """
    INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.com');
    INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.com');
    INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.com');
    
    INSERT INTO Course (title) VALUES ('Python');
    INSERT INTO Course (title) VALUES ('SQL');
    INSERT INTO Course (title) VALUES ('PHP');
    
"""
)

cursor.executescript(
    """
    INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
    
    INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
    
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
"""
)

connection.commit()
