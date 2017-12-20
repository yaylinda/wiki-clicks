from bs4 import BeautifulSoup
from random import sample
import requests

from settings import *

def get_page_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, BEAUTIFUL_SOUP_PARSER)

    subject = soup.find(id = WIKI_HEADING_ID).text

    a_list = soup.find(id = WIKI_CONTENT_ID).find_all("a")
    links = []

    for a in a_list:
        link = a.get("href")
        if link is not None and link.find("/wiki/") == 0 and link.find("File:") == -1:
            links.append(link)

    return (subject, links)

def main():
    url = WIKI_BASE_URL + WIKI_RANDOM_PATH
    iteration = 0
    starting_subject = ""

    while True:
        (subject, links) = get_page_data(url)
        print("%s [%d]" % (subject, len(links)))

        if iteration == 0:
            starting_subject = subject
        else:
            if subject == starting_subject:
                break

        next_url = sample(links, 1)[0]
        url = WIKI_BASE_URL + next_url

        iteration += 1

    print("%d iterations" % iteration)


if __name__ == "__main__":
    main()
