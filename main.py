import requests
from bs4 import BeautifulSoup

from settings import *

page = requests.get(WIKI_RANDOM_URL)
soup = BeautifulSoup(page.text, "html.parser")

subject = soup.find(id = WIKI_HEADING_ID).text
print(subject)

a_list = soup.find(id = WIKI_CONTENT_ID).find_all("a")
wiki_links = []

for a in a_list:
  link = a.get("href")
  if link.find("/wiki/") == 0 and link.find("File:") == -1:
    wiki_links.append(link)

print(wiki_links)
