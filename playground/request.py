import requests
from bs4 import BeautifulSoup


    # Get the html
    response = requests.get("http://py4e-data.dr-chuck.net/comments_42.html")
    response.raise_for_status()
    html = response.text

    # Parse the html
    soup = BeautifulSoup(html, "html.parser")

    # Get the numbers
    nums = []
    for span in soup.find_all("span"):
        nums.append(int(span.getText()))

    # Print sum
    print(sum(nums))
