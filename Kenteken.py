from collections import Counter
import urllib.request
from bs4 import BeautifulSoup

base_link = 'https://www.rdwdata.nl/kenteken/78GSP6'
def get_html(base_link):
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html

def get_info(base_link):
    soup = BeautifulSoup(get_html(base_link),'html.parser')
    kenteken_body=soup.find('div',{'id': 'container'})
    print(kenteken_body)
    for links in kenteken_body:
            (links.find('table'))
     