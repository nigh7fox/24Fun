from collections import Counter
import urllib.request
from bs4 import BeautifulSoup
import csv


base_link = 'https://www.rdwdata.nl/kenteken/78GSP6'
keywords = ['Merk', 'Handelsbenaming', 'Voertuigssoort', 'Brandstof', 'Bouwjaar'] 


def get_html():
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html


def get_info():
    soup = BeautifulSoup(get_html(),'html.parser')
    kenteken_body = soup.find('div', {'class' : 'data small'})
    all_tds = soup.find_all('td')
    keyword_list = []
    keyword_index = []
    kenteken_data = []
    for i, x in enumerate(all_tds):
        if x.string in keywords:
            keyword_index.append(i)
    for y in keyword_index:
        kenteken_data.append(all_tds[y+2].string)
    return list(set(kenteken_data))


def write_to_csv():
    try:
        with open('kenteken_data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(get_info())
    except FileNotFoundError:
        print('ERRROOORRRRR REEEEE')
    finally:
        f.close()

write_to_csv()
