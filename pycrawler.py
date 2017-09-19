import re
import requests
from sys import argv, exit
import parsers


class PyCrawler():
    seed_url = ""
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    to_visit = []
    visited = set()
    max_count = 0

    def __init__(self, seed_url, max_count=0):
        pattern = re.compile(self.url_regex)
        if pattern.match(seed_url):
            self.seed_url = seed_url
            self.to_visit.append(seed_url)
            self.max_count = max_count
        else:
            # Crawler can only be instantiated with valid urls
            exit("Invalid seed url used.")

    def get_request(self, url):
        """
        Send request to get response for a url.
        Returns the response text.
        """
        if url not in self.visited:
            self.visited.add(url)
            try:
                content = requests.get(url)
                if content.status_code == requests.codes.ok:
                    return content.text
            except requests.exceptions.RequestException as e:
                # Handle network errors here
                # Eg. Retry failed requests
                pass

    def start(self):
        """
        Starts running the crawler.
        """
        print "Crawling ..."
        print "Press Ctrl C to exit."
        for url in self.to_visit:
            if self.max_count != 0 and len(self.visited) == self.max_count:
                break
            text = self.get_request(url)
            parsed_dict = parsers.html_parser(text, url)
            if parsed_dict:
                urls = parsed_dict["urls"]
                parsed_html = parsed_dict["html"]
                if urls:
                    self.to_visit.extend(urls)
                if parsed_html:
                    self.parsed_output(parsed_html, url)

    def parsed_output(self, parsed_html, url):
        """
        This function is called by the crawler everytime a
        web page is parsed successfully.
        First argument is the HTML parsed by beautifulsoup.
        Second argument is the url of webpage.
        Override this function in a subclass to change the
        output of the crawler.
        Appends HTML title for every crawled url to a file.
        """
        with open("crawler_output.txt", "a") as output_file:
            title = parsed_html.title
            if title:
                line = url + '  -- ' + title.string + '\n'
                print line
                try:
                    output_file.write(line)
                except:
                    pass


def main():
    if len(argv) == 2:
        seed_url = argv[1]
        crawl = PyCrawler(seed_url)
        crawl.start()
    elif len(argv) == 3:
        seed_url = argv[1]
        try:
            max_count = int(argv[2])
        except:
            print "The second argument must be an integer."
        else:
            crawl = PyCrawler(seed_url, max_count)
            crawl.start()
    else:
        print "Please provide a seed url as the first argument."

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\nBye :)"
