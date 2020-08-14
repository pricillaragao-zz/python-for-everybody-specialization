#  Following Links in Python
#
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The
# program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.
#
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the
# other is the actual data you need to process for the assignment
#
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html Find the link at position 3 (the first
# name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve. Sequence
# of names: Fikret Montgomery Mhairade Butchi Anayah Last name in sequence: Anayah Actual problem: Start at:
# http://py4e-data.dr-chuck.net/known_by_Jesuseun.html Find the link at position 18 (the first name is 1). Follow
# that link. Repeat this process 7 times. The answer is the last name that you retrieve. Hint: The first character of
# the name of the last page that you will load is: S
#
# Strategy
#
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you
# to do the assignment without writing a Python program. But frankly with a little effort and patience you can
# overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But
# that is not the point. The point is to write a clever Python program to solve the program.

# 1 - Download the HTML;
# 2 - Parse the HTML;
# 3 - Select the anchor tags <a>;
# 4 - Extract the href values;
# 5 - Find the link at the position 3, repeat 4 times;
# 6 - Print the last name.

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url: ")
number_of_iterations = int(input("Enter iterations: "))
position = int(input("Enter position: ")) - 1
for _ in range(number_of_iterations):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        anchor_tags = soup.find_all("a")
        url = anchor_tags[position].get("href")
print(url)
