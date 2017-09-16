from pycrawler import PyCrawler
from sys import argv

class MyCrawler(PyCrawler):
    def parsed_output(self, parsed_html, url):
        """
        Saves the title of the page and all html links
        in the page.
        """
        with open("mycrawler_output.txt", "a") as output_file:
            title = parsed_html.title
            urls = []
            for a in parsed_html.find_all('a', href=True):
                url = a['href']
                if url.startswith("http"):
                    urls.append(url)
            url_string = "[" + ", ".join(urls) + "]"
            line = ""
            if title:
                line = url + '  -- ' + title.string + '\n' + url_string + "\n\n"
            else:
                line = url + '  -- ' + "NO TITLE" + '\n' + url_string + "\n\n"
            try:
                output_file.write(line)
            except:
                pass


def main():
    if len(argv) == 2:
        seed_url = argv[1]
        crawl = MyCrawler(seed_url)
        crawl.start()
    elif len(argv) == 3:
        seed_url = argv[1]
        try:
            max_count = int(argv[2])
        except:
            print "The second argument must be an integer."
        else:
            crawl = MyCrawler(seed_url, max_count)
            crawl.start()
    else:
        print "Please provide a seed url as the first argument."


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\nBye :)"