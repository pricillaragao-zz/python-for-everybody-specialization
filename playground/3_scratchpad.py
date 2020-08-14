# 1 - Download the HTML file;
import urllib.request
from bs4 import BeautifulSoup

url = input("Enter: ")
with urllib.request.urlopen(url) as response:
    html = response.read()
    # 2 - Parse the HTML;
    soup = BeautifulSoup(html, "html.parser")

# 3 - Select the numbers;
# 4 - Print the sum.
nums = []
for span in soup.find_all("span"):
    nums.append(int(span.get_text()))
print(sum(nums))
