#  Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute 
# the sum of the numbers. 

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
# and then converting the extracted strings to integers and summing up the integers. 

import re

filename = input('Enter file:')
handle = open(filename)

lst = list()
num_counts = dict()
for line in handle:
  numbers = re.findall('[0-9]+', line)
  if not numbers: 
    continue
  for number in numbers:
    number = int(number)
    # print(number)
    number = lst.append(number)
print(sum(lst))


