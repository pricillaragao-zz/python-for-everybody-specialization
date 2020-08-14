import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = input("Enter - ")
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

soup = BeautifulSoup(html, "html.parser")
# print(soup)
span = soup("span")
for span in soup.find_all("span"):
    # print(tag.get('href', None))
    print(span.getText())
