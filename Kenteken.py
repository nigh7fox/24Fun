from collections import Counter
import urllib.request
import urllib.error
import csv
from bs4 import BeautifulSoup
from ordered_set import OrderedSet

keywords = ['Merk', 'Handelsbenaming', 'Inrichting', 'Brandstof', 'Vermogen', 'Bouwjaar', 'BPM'] 


def get_html(base_link):
    url_request = urllib.request.Request(base_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html


def get_info(base_link):
    soup = BeautifulSoup(get_html(base_link),'html.parser')
    all_tds = soup.find_all('td')
    keyword_index = []
    kenteken_data = []
    for i, x in enumerate(all_tds):
        if x.string in keywords:
            keyword_index.append(i)
    for y in keyword_index:
        kenteken_data.append(all_tds[y+2].string)
    return list(OrderedSet(kenteken_data))


def write_to_csv(a_link):
    try:
        with open('kenteken_data_test.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(get_info(a_link))
    except FileNotFoundError:
        print('ERRROOORRRRR REEEEE')
    finally:
        f.close()


def main():
    base_link = 'https://www.rdwdata.nl/kenteken/'  

    fname = input('Enter filename for number plates')
    
    with open(fname) as f:
        for line in f:
            a_link = base_link + line
            print(a_link)
            if a_link.strip() != base_link.strip():
                try:
                    write_to_csv(a_link)
                except urllib.error.HTTPError:
                    print("bruuuuuuuhhhhhhh")

            else:
                print("Looks empty")
                break
    
          

if __name__ == "__main__":
    main()
