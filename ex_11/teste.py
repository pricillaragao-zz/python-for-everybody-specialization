import re

# x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# y = re.findall("\S+?@\S+", x)
# print(y)

xx = "From: Using the : character"
yy = re.findall("^F.+:", xx)
print(yy)
