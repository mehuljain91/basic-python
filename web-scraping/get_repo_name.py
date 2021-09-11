""" Web Scraping using BeautifulSoup """

import requests
from bs4 import BeautifulSoup as bs

print("Get popular repositories name ")

# take github username as input
github_user = input("Enter Github username: ")
url = "https://github.com/" + github_user

# request url
r = requests.get(url)

# if 404 error 
st_code = r.status_code
if st_code == 404:
    print('Username does not exist')

soup = bs(r.content, 'html.parser')

# find span tag with class repo
spans = soup.find_all('span', class_='repo')
spans_len = len(spans)

for i in range(spans_len):
    print(spans[i].get_text())
