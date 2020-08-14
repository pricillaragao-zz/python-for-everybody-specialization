from collections import Counter

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails_counter = Counter()

for line in handle:
  if not line.startswith("From "):
    continue
  email = line.split()[1]
  emails_counter[email] += 1

most_common_email = emails_counter.most_common()[0]

print(most_common_email[0], most_common_email[1])
