##PyCrawler

####Installation:

1. Create a virtualenv
2. Clone the repo
3. Install requirements

```
virtualenv env
cd env
source ./bin/activate
git clone https://github.com/ankit1ank/pycrawler.git
cd pycrawler
pip install -r requirements.txt
python pycrawler.py http://news.ycombinator.com
```

PyCrawler is a simple web crawler.

By default, pycrawler extracts the title from each url is vists and saves the output in a file named `crawler_output.txt`

#### Advanced Usage:
You can also specify the number of unique urls to visit.

The crawler automatically stops after visiting first 100 urls with the following command:
```
python pycrawler.py http://news.ycombinator.com 100
```

You can change the output of the crawler by subclassing PyCrawler class and overriding the `parsed_output` method.

Look at mycrawler.py to see an example subclass that writes all urls in a page.