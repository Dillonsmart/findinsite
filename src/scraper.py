import requests
from bs4 import BeautifulSoup
from constants import REQUEST_HEADERS, REQUEST_TIMEOUT

sitemap_url = None


def fetch_website(url: str):
    global sitemap_url
    try:
        r = requests.get(url, timeout=REQUEST_TIMEOUT, headers=REQUEST_HEADERS)
        r.raise_for_status()
        sitemap_url = find_sitemap(url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: \n {e}")
        return


def find_sitemap(url: str):
    global sitemap_url
    if sitemap_url is not None:
        return sitemap_url

    common_sitemaps = [
        "/sitemap.xml",
        "/sitemap"
    ]

    for sitemap in common_sitemaps:
        sm_url = url + sitemap
        try:
            r = requests.get(sm_url, timeout=REQUEST_TIMEOUT, headers=REQUEST_HEADERS)
            r.raise_for_status()
            print(f"Sitemap found: {sm_url}")
            return sm_url
        except requests.exceptions.RequestException:
            continue