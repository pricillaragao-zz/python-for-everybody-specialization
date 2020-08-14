name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email_counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    email_counts[email] = email_counts.get(email, 0) + 1

most_emails_sent = max(email_counts, key=email_counts.get)

print(most_emails_sent, email_counts[most_emails_sent])
