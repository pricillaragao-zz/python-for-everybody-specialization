fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
emails = list()

for line in fh:
    if not line.startswith("From "):
        continue
    emails.append(line.split()[1])

for email in emails:
    print(email)
        
print("There were", len(emails), "lines in the file with From as the first word")
