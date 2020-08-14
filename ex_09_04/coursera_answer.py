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

largest = -1
most_recurring_email = None

for email_sent, email_count in email_counts.items():
    if email_count > largest:
        largest = email_count
        most_recurring_email = email

print(email, largest)
