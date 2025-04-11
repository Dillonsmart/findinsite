import requests
from bs4 import BeautifulSoup
from constants import REQUEST_HEADERS, REQUEST_TIMEOUT


def fetch_website(url: str):
    try:
        r = requests.get(url, timeout=REQUEST_TIMEOUT, headers=REQUEST_HEADERS)
        r.raise_for_status()
        parse_webpage(r)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: \n {e}")
        return


def parse_webpage(r: requests.Response):
    soup = BeautifulSoup(r.text, "html.parser")
    page_title = soup.title.string if soup.title else "No title found"
    print(f"Page title: {page_title}")
