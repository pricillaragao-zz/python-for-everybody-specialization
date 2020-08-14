# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

# Hint: make sure not to include the lines that start with 'From:'.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

from pathlib import Path

while True:
    filename = input("Enter file name: ")
    filepath = Path(filename)
    if filepath.exists() and filepath.is_file():
        break
    else:
        print("File does not exists.")

with open(filename) as f:
    emails = list()
    for line in filename:
        if not line.startswith("From "):
            continue
        emails.append(line.split()[1])

for email in emails:
    print(email)

print("There were", len(emails), "lines in the file with From as the first word")
