import re
from bs4 import BeautifulSoup

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def url_parser(text):
        """
        Finds urls in a text file.
        Returns a list of all urls found.
        """
        if text:
            return re.findall(url_regex, text)


def html_parser(text, url):
    """
    Parses html and finds all href links in an html file.
    Return a dictionary with parsed html and urls.
    """
    if text:
        html = BeautifulSoup(text, "html.parser")
        urls = []
        for a in html.find_all('a', href=True):
            url = a['href']
            if url.startswith("http"):
                urls.append(url)
        return {"html": html, "urls": urls}
