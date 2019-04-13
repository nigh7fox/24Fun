import urllib.request
from bs4 import BeautifulSoup


def get_data():
    base_link = 'http://24ora.com/category/local/suceso/'
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html


def get_comments():
    soup = BeautifulSoup(get_data(), 'html.parser')
    suceso_links = []
    suceso_articles = []
    suceso_main = soup.find('div', {'class': 'td-ss-main-content'})
    for y in suceso_main:
        suceso_links.append(y.find('a')['href'])
    for x in suceso_links:
        print(x)
    pass 


def main():
    get_comments()
    return 0


if __name__ == "__main__":
    main()

