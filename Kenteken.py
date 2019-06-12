from collections import Counter
import urllib.request
from bs4 import BeautifulSoup

base_link = 'https://www.rdwdata.nl/kenteken/78GSP6'
def get_html():
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html

def get_info():
    soup = BeautifulSoup(get_html(),'html.parser')
    kenteken_body = soup.find('div', {'class' : 'data small'})
    table_list = []
    for types in kenteken_body:
            if type(types.find('table')) is not int and :
                    table_list.append(types.find('table'))

    for i in table_list:
            if i is not None:
                    print (i[i.find('td>'):])
    
get_info()