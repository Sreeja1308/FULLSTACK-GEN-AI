import requests
from bs4 import BeautifulSoup
url="https://www.mongodb.com/"

headers={
    "User-Agent":"Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print("status code:", response.status_code)

soup = BeautifulSoup(response.content,"html.parser")
print(soup.prettify())

for link in soup.find_all('a'):
  print(link.get('href'))