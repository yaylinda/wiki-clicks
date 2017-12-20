import requests
from bs4 import BeautifulSoup

from settings import *

def get_page_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, BEAUTIFUL_SOUP_PARSER)

    subject = soup.find(id = WIKI_HEADING_ID).text

    a_list = soup.find(id = WIKI_CONTENT_ID).find_all("a")
    wiki_links = []

    for a in a_list:
        link = a.get("href")
        if link is not None and link.find("/wiki/") == 0 and link.find("File:") == -1:
            wiki_links.append(link)

    return (subject, wiki_links)

def main():
    url = WIKI_BASE_URL + WIKI_RANDOM_PATH
    (subject, wiki_links) = get_page_data(url)

if __name__ == "__main__":
    main()
