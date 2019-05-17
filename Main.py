from collections import Counter
import urllib.request
from bs4 import BeautifulSoup


def get_data(base_link):
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html


def get_24ora_page_titles(base_link):
    soup = BeautifulSoup(get_data(base_link), 'html.parser')
    suceso_links = []
    suceso_articles = []
    suceso_main = soup.find('div', {'class': 'td-ss-main-content'})
    for y in suceso_main:
        if type(y.find('a')) is int:
            continue
        else:
            suceso_links.append(y.find('a')['href'])
    return suceso_links


def get_title_words(start, end):
    base_link = 'http://24ora.com/category/local/suceso/'
    titles_arr = []
    title_words = []
    for i in range(start, end):
        for y in get_24ora_page_titles(base_link + 'page/' + str(i)):
            title_not_split = y.strip('/').split('/', 3)[3]
            title_split = title_not_split.split('-')
            titles_arr.append(title_split)
    for titles in titles_arr:
        for words in titles:
            if len(words) > 2:
                title_words.append(words)
    return title_words


def count_words(word_list):
    return sorted(dict(Counter(word_list)).items(), key=lambda x: x[1], reverse=True)
 

def main():
    title_words = get_title_words(0, 100)
    for k, v in count_words(title_words):
        if v > 10:
            print('{} - {}'.format(k, v))
    return 0


if __name__ == "__main__":
    main()

