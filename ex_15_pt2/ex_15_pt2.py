# To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
# (Must have a .sqlite suffix)
# Hint: The top organizational count is 536.
#
# You do not need to export or convert the database - simply upload the .sqlite file that your program creates.
# See the example code for the use of the connect() statement.
#
# Counting Organizations
#
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#
# CREATE TABLE Counts (org TEXT, count INTEGER)
#
# When you have run the program on mbox.txt upload the resulting database file above for grading.
#
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each
# run.
#
# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
#
# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
#
# Because the sample code is using an UPDATE statement and committing the results to the database as each record is
# read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely
# writing all the data to disk every time it is called.
#
# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program,
# there is a balance between the number of operations you execute between commits and the importance of not losing the
# results of operations that have not yet been committed.

# Problem
# 1 - Submit a database with a table called 'Counts' with columns 'org' (text) and 'count (integer). The 'org' column
#     should contain the emails from this dataset https://www.py4e.com/code3/mbox.txt . The database name should
#     have the suffix 'sqlite'
# 2 - Submit a query to select the records ordered by count descending

# Algorithm
# 1 - Create a database named "emails.sqlite"; C
# 2 - Create a table named "Counts" with columns "org" and "count in the database; C
# 3 - Read the file mbox.txt; C
# 4 - Find the received emails; C
# 5 -

# with open("emails.sqlite") as f:


import sqlite3
from pathlib import Path
import re

db_name = "emails.sqlite"
Path(db_name).touch()

conn = sqlite3.connect(db_name)
conn.execute("DROP TABLE Counts;")
conn.execute("CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER);")
conn.execute("DELETE FROM Counts;")
cursor = conn.cursor()

emails_counter = {}
with open("mbox.txt") as email_box:
    for line in email_box:
        if line.startswith("From: "):
            email = line.split("@")[1]
            print(email)
            if email in emails_counter:
                emails_counter[email] += 1
            else:
                emails_counter[email] = 1
for email, count in emails_counter.items():
    cursor.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (email, count))

conn.commit()
cursor.close()


# import sqlite3
#
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')
#
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#
# cur.close()
