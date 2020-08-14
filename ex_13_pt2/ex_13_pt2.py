#  Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The
# program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment
# counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.
#
#     Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_745448.json (Sum ends with 25)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#
# Data Format
#
# The data consists of a number of names and comment counts in JSON as follows:
#
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
#
# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at
# geoxml.py to see how to prompt for a URL and retrieve data from a URL.

# 0 - Enter location
# 1 - Download data in JSON format C
# 2 - Parse JSON C
# 3 - Collect the comment counts from the data C
# 4 - Print the number of counts
# 5 - Print the sum of counts

# 1 - Download the JSON data from a URL;
# 2 - Read the JSON data using URLLIB;
# 3 - Parse the JSON;
# 4 - Collect the comment counts from the JSON data in a list;
# 5 - Find the counts length;
# 6 - Sum the counts content.

import json
import urllib
import urllib.request

url = input("Enter location:")
print("Retrieving", url)
with urllib.request.urlopen(url) as response:
    response_body = response.read().decode()
    print("Retrieved", len(response_body), "characters")
    data = json.loads(response_body)
    comments = data["comments"]
    # print(f"counts: {len(comments)}")
    # print(f"sum: {sum([comment['count'] for comment in comments])}")
    counts = []
    for comment in comments:
        counts.append(comment['count'])
    print(f"Counts: {len(counts)}")
    print(f"Sum: {sum(counts)}")


