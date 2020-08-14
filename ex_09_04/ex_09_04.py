# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

from pathlib import Path

while True:
    name = input("Enter file name: ")
    filepath = Path(name)
    if filepath.exists() and filepath.is_file():
        break
    else:
        print("File does not exists.")

with open(name) as handle:
    emails = (
        list()
    )  # made a list with From emails (Olhar a resposta do coursera -> não precisa fazer a lista e depois o dicionário, pode fazer o dicionário direto.)
    counts = dict()
    for line in handle:
        if not line.startswith("From "):
            continue
        emails.append(line.split()[1])
        # print(line)

    for email in emails:
        # print(email)
        counts[email] = counts.get(email, 0) + 1  # made a dictionary from the list
    # print(counts)

    largest = -1
    most_recurring_email = None
    for email_sent, email_count in counts.items():
        # print(email_sent, amount_sent)
        if email_count > largest:  # selected the most recurring From email
            largest = email_count
            most_recurring_email = email

print(email, largest)
