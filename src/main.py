from argparse import ArgumentParser
from scraper import fetch_website


def main(website_url: str):
    fetch_website(website_url)


if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("--url", type=str, help="The websites URL to scrape")

    url = args.parse_args().url

    if url is None:
        print("No URL provided")
        exit(1)

    main(url)
