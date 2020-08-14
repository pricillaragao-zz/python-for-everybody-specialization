# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to
# http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.

#     Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_745445.html (Sum ends with 77)

# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# 1 - Download the HTML file;
# 2 - Parse the HTML;
# 3 - Select the numbers;
# 4 - Print the sum.

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter: ")
with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    nums = []
    for span in soup.find_all("span"):
        nums.append(int(span.get_text()))
    print(sum(nums))
