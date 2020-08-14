name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

hour_counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    hour = line.split()[5][0:2]
    hour_counts[hour] = hour_counts.get(hour, 0) + 1

for hour, hour_amount in sorted(hour_counts.items()):
    print(hour, hour_amount)
