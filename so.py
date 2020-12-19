import requests
from bs4 import BeautifulSoup

URL = f"https://www.stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    for page in pages:
        print(page.find("span").string)


def get_jobs():
    last_page = get_last_page()
    return []
